# src/core/face_processor.py

import os
import sys
import cv2
import numpy as np
from typing import Optional, List, Dict, Any, Tuple
import insightface
from insightface.app import FaceAnalysis
from insightface.app.common import Face
import platform
import time
from src import get_resource_path

class ExtendedFace(Face):
    """Extended Face class that allows for normalized embedding storage"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._normed_embedding = None
    
    @property
    def normed_embedding(self):
        if self._normed_embedding is None and hasattr(self, 'embedding'):
            # Ensure embedding is float32
            embedding = self.embedding.astype(np.float32)
            self._normed_embedding = embedding / np.linalg.norm(embedding)
        return self._normed_embedding
    
    @normed_embedding.setter
    def normed_embedding(self, value):
        self._normed_embedding = value.astype(np.float32) if value is not None else None

class FaceProcessor:
    def __init__(self):
        """Initialize face processing components with enhanced quality settings"""
        try:
            print("\nInitializing FaceProcessor...")
            self.face_mappings = {}
            self.models_dir = self._get_models_dir()
            self.execution_provider = self._get_execution_provider()
            self._similarity_threshold = 0.2  # Lower default threshold
            # Initialize face analyzer with higher resolution
            print("Loading face analyzer...")
            self.face_analyzer = FaceAnalysis(
                name='buffalo_l',
                providers=[self.execution_provider],
                allowed_modules=['detection', 'recognition', 'landmark_2d_106']  # Explicitly include landmark
            )
            self.prev_face_positions = []
            self.position_smoothing_window = 3
            self.position_threshold = 10.0  # pixels

            self.face_analyzer.prepare(ctx_id=0, det_size=(640, 640))
            print("Face analyzer ready")
            
            # Load face swapper model
            print("Loading face swapper model...")
            model_path = os.path.join(self.models_dir, 'inswapper_128.onnx')
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found: {model_path}")
            
            self.face_swapper = insightface.model_zoo.get_model(
                model_path,
                providers=[self.execution_provider]
            )
            
            # Enhanced similarity settings
            self.similarity_threshold = 0.1  # Lower threshold for better matching
            self.cache_size = 10  # Increased cache size
            self.process_every_n_frames = 1  # Process every frame
            
            # Face detection settings
            self.detection_threshold = 0.5  # Increased confidence threshold
            self.min_face_size = 20  # Minimum face size to process

            # Add face tracking
            self.last_face_location = None
            self.last_successful_swap = None
            self.face_track_threshold = 50  # pixels
            self.stable_frames_required = 3
            self.stable_frame_count = 0            
            # Image enhancement settings
            self.use_face_enhancement = True
            self.enhancement_level = 1.0  # Adjustable enhancement strength
            self.similarity_threshold = 0.5

            print("FaceProcessor initialization complete with enhanced settings")
            
        except Exception as e:
            print(f"Error initializing FaceProcessor: {str(e)}")
            raise
    
    def set_debug_mode(self, enabled: bool) -> None:
        """Enable or disable debug visualization"""
        print(f"Setting debug mode to: {enabled}")
        self.debug_mode = enabled

    def get_debug_mode(self) -> bool:
        """Get current debug mode status"""
        return self.debug_mode
    
    def smooth_face_position(self, current_bbox):
        """Apply temporal smoothing to face positions"""
        if not self.prev_face_positions:
            self.prev_face_positions.append(current_bbox)
            return current_bbox
            
        # Convert to center point
        curr_center = [(current_bbox[0] + current_bbox[2])/2, 
                    (current_bbox[1] + current_bbox[3])/2]
                    
        # Calculate smoothed position
        smoothed_center = curr_center
        if len(self.prev_face_positions) > 0:
            prev_centers = [[(box[0] + box[2])/2, (box[1] + box[3])/2] 
                        for box in self.prev_face_positions]
            
            # Check if movement is within threshold
            prev_center = prev_centers[-1]
            movement = np.sqrt((curr_center[0] - prev_center[0])**2 + 
                            (curr_center[1] - prev_center[1])**2)
                            
            if movement < self.position_threshold:
                # Apply smoothing
                weights = np.linspace(0.5, 1.0, len(prev_centers) + 1)
                weights = weights / weights.sum()
                
                smoothed_x = np.average([c[0] for c in prev_centers + [curr_center]], 
                                    weights=weights)
                smoothed_y = np.average([c[1] for c in prev_centers + [curr_center]], 
                                    weights=weights)
                smoothed_center = [smoothed_x, smoothed_y]
        
        # Update position history
        self.prev_face_positions.append(current_bbox)
        if len(self.prev_face_positions) > self.position_smoothing_window:
            self.prev_face_positions.pop(0)
            
        # Convert back to bbox
        width = current_bbox[2] - current_bbox[0]
        height = current_bbox[3] - current_bbox[1]
        return [
            smoothed_center[0] - width/2,
            smoothed_center[1] - height/2,
            smoothed_center[0] + width/2,
            smoothed_center[1] + height/2
        ]

    def set_face_mappings(self, mappings: Dict[str, Any]) -> None:
        """Update the face mappings dictionary with validation"""
        print("\nSetting face mappings:")
        print(f"Received {len(mappings)} mappings")
        
        self.face_mappings = {}
        
        for mapping_id, mapping in mappings.items():
            print(f"\nProcessing mapping {mapping_id}:")
            try:
                if 'source_face' in mapping and mapping['source_face'] is not None:
                    source_face = mapping['source_face']
                    # print(f"Source face keys: {list(source_face.keys())}")
                    
                    # Verify we have the minimum required data
                    if 'embedding' not in source_face:
                        print("No embedding found in source face")
                        continue
                        
                    # Store the mapping
                    self.face_mappings[mapping_id] = {
                        'source_face': source_face
                    }
                    print(f"Successfully added mapping {mapping_id}")
                else:
                    print("No source_face data in mapping")
                    
            except Exception as e:
                print(f"Error processing mapping {mapping_id}: {str(e)}")
                import traceback
                traceback.print_exc()
                continue
                
        print(f"\nTotal face mappings stored: {len(self.face_mappings)}")
        for mapping_id in self.face_mappings:
            print(f"- {mapping_id}")
        
    def detect_faces(self, frame: np.ndarray) -> List[dict]:
        """Detect and analyze faces in a frame"""
        if frame is None:
            print("Frame is None")
            return []
                
        try:
            # print(f"Frame shape: {frame.shape}")
            # print(f"Frame dtype: {frame.dtype}")
            # print("Attempting face detection...")
            faces = self.face_analyzer.get(frame)
            # print(f"Detected {len(faces)} faces")
            return [{
                'face': face,
                'bbox': face.bbox,
                'embedding': face.normed_embedding,
                'landmarks': face.landmark_2d_106
            } for face in faces]
        except Exception as e:
            print(f"Error detecting faces: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
        
    # Update in src/core/face_processor.py

    def find_best_match(self, target_embedding: np.ndarray) -> Optional[Dict[str, Any]]:
        """Find the best matching source face for a target embedding"""
        try:
            # print("\n=== Starting Face Matching Process ===")
            # print(f"Current similarity threshold: {self.similarity_threshold}")
            # print(f"Number of face mappings: {len(self.face_mappings)}")
            # print("Available mappings:", list(self.face_mappings.keys()))

            if not self.face_mappings:
                # print("No face mappings available")
                return None

            if target_embedding is None:
                print("Target embedding is None")
                return None

            # Convert and normalize target embedding
            if isinstance(target_embedding, list):
                target_embedding = np.array(target_embedding)
            target_embedding = target_embedding.astype(np.float32)
            target_embedding = target_embedding / np.linalg.norm(target_embedding)

            # print("\nTarget Embedding Stats:")
            # print(f"Shape: {target_embedding.shape}")
            # print(f"Norm: {np.linalg.norm(target_embedding):.4f}")

            best_match = None
            best_similarity = -1

            for mapping_id, mapping in self.face_mappings.items():
                # print(f"\nProcessing mapping {mapping_id}:")
                
                if 'source_face' not in mapping:
                    print("- No source_face in mapping")
                    continue
                    
                source_data = mapping['source_face']
                # print("- Source face keys:", list(source_data.keys()))
                
                source_embedding = source_data.get('embedding')
                if source_embedding is None:
                    print("- No embedding in source face")
                    continue

                # Convert and normalize source embedding
                if isinstance(source_embedding, list):
                    source_embedding = np.array(source_embedding)
                source_embedding = source_embedding.astype(np.float32)
                source_embedding = source_embedding / np.linalg.norm(source_embedding)

                # Calculate similarity
                similarity = abs(float(np.dot(target_embedding, source_embedding)))
                
                # print(f"- Calculated similarity: {similarity:.4f}")

                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = {
                        'mapping_id': mapping_id,
                        'source_face': source_data,
                        'similarity': similarity
                    }
                    # print(f"- New best match! Similarity: {similarity:.4f}")

            if best_match:
                # print(f"\nFinal Best Match:")
                # print(f"- Mapping ID: {best_match['mapping_id']}")
                # print(f"- Similarity: {best_match['similarity']:.4f}")
                # print(f"- Threshold: {self.similarity_threshold}")
                
                if best_match['similarity'] > self.similarity_threshold:
                    # print("Match ACCEPTED")
                    return best_match
                else:
                    print("Match REJECTED (below threshold)")
            else:
                print("\nNo matches found")

            return None

        except Exception as e:
            print(f"Error in find_best_match: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def _get_models_dir(self) -> str:
        """Get the appropriate models directory based on environment"""
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            return os.path.join(sys._MEIPASS, 'models')
        else:
            # Running in development
            return os.path.join(os.path.dirname(os.path.dirname(
                os.path.dirname(__file__))), 'models')

    def _get_execution_provider(self) -> str:
        """Determine the best execution provider for the current system"""
        if platform.processor() == 'arm':
            return 'CoreMLExecutionProvider'
        return 'CPUExecutionProvider'
    
    # def reconstruct_face(self, face_dict):
    #     """Reconstruct a Face object from a dictionary representation"""
    #     try:
    #         if face_dict is None:
    #             print("Face dict is None")
    #             return None

    #         print("\nReconstructing face:")
    #         print(f"Input data: {type(face_dict)}")
            
    #         # Create a basic Face object (with empty image)
    #         face = Face()
            
    #         if isinstance(face_dict, dict):
    #             print("Processing face dictionary...")
                
    #             # Handle nested face_dict structure
    #             if 'face_dict' in face_dict:
    #                 face_data = face_dict['face_dict']
    #             else:
    #                 face_data = face_dict
                    
    #             # Set required attributes
    #             if 'embedding' in face_data:
    #                 face.embedding = np.array(face_data['embedding'])
    #                 face.normed_embedding = face.embedding / np.linalg.norm(face.embedding)
    #                 face.embedding_norm = np.linalg.norm(face.embedding)
    #                 print("Set embedding attributes")
                    
    #             if 'bbox' in face_data:
    #                 face.bbox = np.array(face_data['bbox'])
    #                 print("Set bbox")
                    
    #             if 'kps' in face_data:
    #                 face.kps = np.array(face_data['kps'])
    #                 print("Set keypoints")
                    
    #             if 'landmark_2d_106' in face_data:
    #                 face.landmark_2d_106 = np.array(face_data['landmark_2d_106'])
    #                 print("Set landmarks")
                    
    #             # Set additional required attributes
    #             face.det_score = face_data.get('det_score', 0.99)  # Default high score
    #             face.pose = face_data.get('pose', np.zeros(3))     # Default neutral pose
    #             face.num_det = 1                                   # Single detection
                
    #             print("\nReconstructed face verification:")
    #             print(f"- Has bbox: {hasattr(face, 'bbox')}")
    #             print(f"- Has embedding: {hasattr(face, 'embedding')}")
    #             print(f"- Has normed_embedding: {hasattr(face, 'normed_embedding')}")
    #             if hasattr(face, 'embedding'):
    #                 print(f"- Embedding shape: {face.embedding.shape}")
    #                 print(f"- Embedding norm: {face.embedding_norm:.4f}")
                
    #             return face
                    
    #         else:
    #             print(f"Invalid face_dict type: {type(face_dict)}")
    #             return None
                
    #     except Exception as e:
    #         print(f"Error reconstructing face: {str(e)}")
    #         import traceback
    #         traceback.print_exc()
    #         return None

    def reconstruct_face(self, source_face):
        """
        Reconstructs a face from a dictionary representation for face swapping
        Args:
            self: FaceProcessor instance
            source_face: Dictionary containing face data and embedding info
        Returns:
            ExtendedFace: Face object with computed normed_embedding
        """
        try:
            # Get the actual face dictionary from the nested structure
            face_dict = source_face.get('face_dict', {})
            
            # Create new face object
            face = ExtendedFace()
            
            # Set face properties from the face dictionary
            for key, value in face_dict.items():
                if key == 'embedding':
                    # Ensure embedding is float32
                    value = np.array(value, dtype=np.float32)
                elif key == 'normed_embedding':
                    continue  # Skip normed_embedding as it will be calculated
                elif isinstance(value, np.ndarray):
                    # Convert any numpy arrays to float32
                    value = value.astype(np.float32)
                setattr(face, key, value)
            
            # If embedding wasn't in face_dict but exists in source_face, use that
            if not hasattr(face, 'embedding') and 'embedding' in source_face:
                face.embedding = np.array(source_face['embedding'], dtype=np.float32)
            
            # Verify embedding exists and compute normalized version
            if hasattr(face, 'embedding'):
                _ = face.normed_embedding  # This will trigger the property to compute the normalized embedding
                return face
            else:
                print("No embedding found in face data")
                return None
                
        except Exception as e:
            print(f"Error reconstructing face: {str(e)}")
            return None


    def process_frame(self, frame):
        """Process a frame for face swapping"""
        if frame is None:
            return frame
            
        try:
            result = frame.copy()
            current_faces = self.detect_faces(frame)
            
            if not current_faces:
                return self.draw_debug_info(frame, []) if self.debug_mode else frame
 
                
            swapped = result.copy()
            swap_successful = False
            
            for face_data in current_faces:
                # Ensure face_data embedding is float32
                if 'embedding' in face_data:
                    face_data['embedding'] = np.array(face_data['embedding'], dtype=np.float32)
                
                match = self.find_best_match(face_data['embedding'])
                if match and match['similarity'] > self.similarity_threshold:
                    try:
                        # print("\nGot a match, preparing face swap...")
                        source_face = match['source_face']
                        
                        # Add source embedding to the face dict if not present
                        if isinstance(source_face, dict) and 'face_dict' in source_face:
                            if 'embedding' not in source_face['face_dict']:
                                source_face['face_dict']['embedding'] = np.array(source_face['embedding'], dtype=np.float32)
                        
                        # Ensure we have a proper Face object
                        if not isinstance(source_face, Face):
                            # print("Reconstructing face from dictionary...")
                            source_face = self.reconstruct_face(source_face)
                        
                        if source_face is not None:
                            # print("Attempting face swap...")
                            swapped = self.face_swapper.get(
                                swapped,
                                face_data['face'],
                                source_face,
                                paste_back=True
                            )
                            swap_successful = True
                            # print("Face swap successful!")
                        else:
                            print("Failed to reconstruct source face")
                            
                    except Exception as e:
                        print(f"Error in face swap: {str(e)}")
                        import traceback
                        traceback.print_exc()
                        continue
                        
            return swapped if swap_successful else result
            
        except Exception as e:
            print(f"Error in process_frame: {str(e)}")
            import traceback
            traceback.print_exc()
            return frame

    def extract_face(self, frame: np.ndarray, bbox) -> Optional[np.ndarray]:
        """Extract face region from frame"""
        try:
            x1, y1, x2, y2 = map(int, bbox)
            return frame[y1:y2, x1:x2]
        except Exception as e:
            print(f"Error extracting face: {str(e)}")
            return None
        
    def analyze_face(self, image):
        """Analyze a face in an image"""
        try:
            # print("\nAnalyzing face...")
            faces = self.face_analyzer.get(image)
            
            if not faces:
                print("No faces detected")
                return None
                
            face = faces[0]  # Get the first face
            
            # Create face dictionary with safe attribute access
            face_dict = {}
            
            # Safely get embedding (most important)
            if hasattr(face, 'embedding') and face.embedding is not None:
                face_dict['embedding'] = face.embedding.tolist()
            else:
                print("No embedding found - this is required")
                return None
                
            # Safely get other attributes
            if hasattr(face, 'bbox') and face.bbox is not None:
                face_dict['bbox'] = face.bbox.tolist()
                
            if hasattr(face, 'kps') and face.kps is not None:
                face_dict['kps'] = face.kps.tolist()
                
            if hasattr(face, 'det_score'):
                face_dict['det_score'] = float(face.det_score)
                
            # Handle landmark_2d_106 carefully since it's failing
            if hasattr(face, 'landmark_2d_106') and face.landmark_2d_106 is not None:
                try:
                    face_dict['landmark_2d_106'] = face.landmark_2d_106.tolist()
                except:
                    print("Warning: Could not process landmark_2d_106")
                    face_dict['landmark_2d_106'] = None
            else:
                face_dict['landmark_2d_106'] = None
                
            if hasattr(face, 'pose') and face.pose is not None:
                face_dict['pose'] = face.pose.tolist()
                
            face_dict['gender'] = face.gender if hasattr(face, 'gender') else -1
            face_dict['num_det'] = face.num_det if hasattr(face, 'num_det') else 1
            
            print(f"Face data extracted:")
            for key, value in face_dict.items():
                if value is not None:
                    if isinstance(value, list):
                        print(f"- {key}: list of length {len(value)}")
                    else:
                        print(f"- {key}: {type(value)}")
                        
            return {
                'face': face,  # Keep original face object for immediate use
                'face_dict': face_dict,  # Store serializable dict for later
                'embedding': face.embedding,
                'image': image
            }
            
        except Exception as e:
            print(f"Error analyzing face: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
        
    def draw_debug_info(self, frame: np.ndarray, faces: List[dict]) -> np.ndarray:
        """Draw debug information on frame if debug mode is enabled"""
        if not self.debug_mode:
            return frame
            
        debug_frame = frame.copy()
        
        try:
            for face_data in faces:
                # Draw bounding box if available
                if 'bbox' in face_data:
                    bbox = face_data['bbox']
                    x1, y1, x2, y2 = map(int, bbox)
                    cv2.rectangle(debug_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # Add confidence score if available
                    if 'det_score' in face_data:
                        score = face_data['det_score']
                        score_text = f"Conf: {score:.2f}"
                        cv2.putText(debug_frame, score_text, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    
                # Draw landmarks if available
                if 'landmark_2d_106' in face_data and face_data['landmark_2d_106'] is not None:
                    landmarks = face_data['landmark_2d_106']
                    for point in landmarks:
                        x, y = map(int, point)
                        cv2.circle(debug_frame, (x, y), 1, (0, 0, 255), -1)
                        
                # Draw face center if available
                if 'bbox' in face_data:
                    bbox = face_data['bbox']
                    center_x = int((bbox[0] + bbox[2]) / 2)
                    center_y = int((bbox[1] + bbox[3]) / 2)
                    cv2.circle(debug_frame, (center_x, center_y), 3, (255, 0, 0), -1)
                    
        except Exception as e:
            print(f"Error drawing debug info: {str(e)}")
            return frame
            
        return debug_frame

    def set_source_face(self, image: np.ndarray) -> bool:
        """Set the source face for swapping"""
        if image is None:
            print("No image provided")
            return False
        
        try:
            faces = self.face_analyzer.get(image)
            if not faces:
                print("No faces detected in source image")
                return False
            
            # Get the most prominent face
            self.source_face = min(faces, key=lambda x: x.bbox[0])
            self.source_embedding = self.source_face.normed_embedding
            return True
        
        except Exception as e:
            print(f"Error setting source face: {e}")
            return False

    def get_face_preview(self, face) -> Optional[np.ndarray]:
        """Extract face region for preview"""
        if face is None:
            return None
        
        try:
            if not hasattr(face, 'bbox'):
                return None
            
            x1, y1, x2, y2 = map(int, face.bbox)
            if not hasattr(face, 'img') or face.img is None:
                return None
            
            return face.img[y1:y2, x1:x2]
        
        except Exception as e:
            print(f"Error getting face preview: {e}")
            return None

    def draw_debug_info(self, frame: np.ndarray, faces: List[Dict[str, Any]]) -> np.ndarray:
        """Draw debug information on frame"""
        debug_frame = frame.copy()
        for face in faces:
            bbox = face['bbox']
            x1, y1, x2, y2 = map(int, bbox)
            
            # Draw bounding box
            cv2.rectangle(debug_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw landmarks
            if 'landmarks' in face:
                for point in face['landmarks']:
                    x, y = map(int, point)
                    cv2.circle(debug_frame, (x, y), 1, (0, 0, 255), -1)
            
            # Add text for face information
            text = "Target Face"
            cv2.putText(debug_frame, text, (x1, y1 - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return debug_frame

    def set_debug_mode(self, enabled: bool) -> None:
        """Enable or disable debug visualization"""
        self.debug_mode = enabled
        print(f"Debug mode {'enabled' if enabled else 'disabled'}")

    def preprocess_embedding(self, embedding: np.ndarray) -> Optional[np.ndarray]:
        """Preprocess face embedding for better matching"""
        try:
            print("\nPreprocessing embedding...")
            
            # Convert to numpy array if needed
            if isinstance(embedding, list):
                print("Converting list to numpy array")
                embedding = np.array(embedding)
            
            if embedding is None:
                print("Embedding is None")
                return None
                
            if not isinstance(embedding, np.ndarray):
                print(f"Unexpected embedding type: {type(embedding)}")
                return None

            # Ensure embedding is float32
            embedding = embedding.astype(np.float32)
            print(f"Converted to float32, shape: {embedding.shape}")
            
            # L2 normalization
            norm = np.linalg.norm(embedding)
            print(f"Initial norm: {norm}")
            
            if norm > 0:
                embedding = embedding / norm
                print(f"Normalized, new norm: {np.linalg.norm(embedding)}")
                return embedding
            else:
                print("Zero norm encountered")
                return None
                
        except Exception as e:
            print(f"Error preprocessing embedding: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def _match_faces_between_frames(self, current_faces, previous_faces):
        """Check if faces in current frame match previous frame"""
        if not current_faces or not previous_faces:
            return False
        
        try:
            # Check if number of faces matches
            if len(current_faces) != len(previous_faces):
                return False
            
            # Check each face position
            for curr, prev in zip(current_faces, previous_faces):
                curr_center = self._get_face_center(curr['bbox'])
                prev_center = self._get_face_center(prev['bbox'])
                
                # Calculate position shift
                shift = np.sqrt(
                    (curr_center[0] - prev_center[0])**2 +
                    (curr_center[1] - prev_center[1])**2
                )
                
                # If shift is too large, faces don't match
                if shift > self.max_position_shift:
                    return False
                
            return True
        
        except Exception as e:
            print(f"Error matching faces: {e}")
            return False

    def _get_face_center(self, bbox):
        """Calculate center point of face bounding box"""
        x1, y1, x2, y2 = bbox
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def reset_face_cache(self):
        """Reset the face caching"""
        self.last_successful_faces = None

    def verify_face_objects(self, source_face, target_face) -> bool:
        """Verify face objects have required attributes"""
        try:
            # Check source face
            if source_face is None:
                print("Source face is None")
                return False
            
            # Check target face
            if target_face is None:
                print("Target face is None")
                return False
            
            # Check required attributes
            required_attrs = ['bbox', 'landmark_2d_106', 'embedding']
            
            for attr in required_attrs:
                if not hasattr(source_face, attr):
                    print(f"Source face missing {attr}")
                    return False
                if not hasattr(target_face, attr):
                    print(f"Target face missing {attr}")
                    return False
                
            return True
        
        except Exception as e:
            print(f"Error verifying face objects: {str(e)}")
            return False

    def test_face_swapper(self):
        """Test face swapper functionality"""
        try:
            print("\nTesting face swapper...")
            # Create a simple test image
            test_img = np.zeros((128, 128, 3), dtype=np.uint8)
            test_img = cv2.rectangle(test_img, (30, 30), (98, 98), (255, 255, 255), -1)
            
            # Test if the model is responsive
            print("Testing model response...")
            result = self.face_swapper.get_input_shape()
            print(f"Model input shape: {result}")
            
            print("Face swapper test complete")
            return True
            
        except Exception as e:
            print(f"Face swapper test failed: {str(e)}")
            return False

    def enhance_face_region(self, image, bbox, strength=1.0):
        """Apply enhancement to the face region"""
        try:
            x1, y1, x2, y2 = map(int, bbox)
            face_region = image[y1:y2, x1:x2]
            
            # Apply subtle sharpening
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]]) * strength
            sharpened = cv2.filter2D(face_region, -1, kernel)
            
            # Blend the sharpened region with original
            enhanced = cv2.addWeighted(face_region, 0.7, sharpened, 0.3, 0)
            
            # Place enhanced region back
            result = image.copy()
            result[y1:y2, x1:x2] = enhanced
            return result
            
        except Exception as e:
            print(f"Error enhancing face region: {e}")
            return image

def preprocess_celebrities(face_processor, images_dir, max_images_per_celebrity=3):
    """Preprocess celebrity images and return mappings for the gallery."""
    import os
    import cv2
    import numpy as np
    import random

    def load_celebrity_images(images_dir, max_images):
        """Load a limited number of celebrity images from the specified directory."""
        celebrities = {}
        images_dir = get_resource_path('images')
        for celebrity in os.listdir(images_dir):
            celebrity_dir = os.path.join(images_dir, celebrity)
            if os.path.isdir(celebrity_dir):
                # Collect all images in the celebrity's directory
                all_images = [
                    os.path.join(celebrity_dir, file)
                    for file in os.listdir(celebrity_dir)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))
                ]
                if all_images:
                    # Randomly select up to max_images
                    selected_images = random.sample(all_images, min(max_images, len(all_images)))
                    celebrities[celebrity] = selected_images
        return celebrities

    print("\nLoading celebrity images...")
    celebrity_images = load_celebrity_images(images_dir, max_images_per_celebrity)
    predefined_faces = {}

    for celebrity, images in celebrity_images.items():
        print(f"\nProcessing {celebrity}...")
        embeddings = []
        valid_faces = []
        preview_image = None

        # Process each image for the celebrity
        for img_path in images:
            try:
                image = cv2.imread(img_path)
                if image is not None:
                    face_data = face_processor.analyze_face(image)
                    if face_data:
                        embeddings.append(face_data['embedding'])
                        valid_faces.append(face_data['face'])
                        if preview_image is None:
                            preview_image = img_path  # Store the first successful image path
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")

        if embeddings and preview_image:
            # Create an average embedding from all valid faces
            avg_embedding = np.mean(embeddings, axis=0)
            # Normalize the average embedding
            avg_embedding = avg_embedding / np.linalg.norm(avg_embedding)
            
            predefined_faces[celebrity] = {
                "preview_image": preview_image,  # Store the image path
                "embedding": avg_embedding,
                "all_embeddings": embeddings,
                "all_faces": valid_faces
            }
            print(f"Processed {len(embeddings)} faces for {celebrity}")

    return predefined_faces
