# src/core/face_processor.py

import os
import sys
import cv2
import numpy as np
from typing import Optional, List, Dict, Any, Tuple
import insightface
from insightface.app import FaceAnalysis
import platform
import time

class FaceProcessor:
    def __init__(self):
        """Initialize face processing components"""
        try:
            print("\nInitializing FaceProcessor...")
            self.face_mappings = {}  # Initialize face mappings
            self.models_dir = self._get_models_dir()
            self.execution_provider = self._get_execution_provider()
            
            # Initialize face analyzer
            print("Loading face analyzer...")
            self.face_analyzer = FaceAnalysis(
                name='buffalo_l',
                providers=[self.execution_provider]
            )
            self.face_analyzer.prepare(ctx_id=0, det_size=(640, 640))
            print("Face analyzer ready")
            
            # Load face swapper model
            print("Loading face swapper model...")
            model_path = os.path.join(self.models_dir, 'inswapper_128.onnx')
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found: {model_path}")
            
            print(f"Loading model from: {model_path}")
            print(f"Using execution provider: {self.execution_provider}")
            
            self.face_swapper = insightface.model_zoo.get_model(
                model_path,
                providers=[self.execution_provider]
            )
            
            # Verify face swapper loaded correctly
            if self.face_swapper is None:
                raise RuntimeError("Face swapper failed to initialize")
            
            print("Face swapper loaded successfully")
            print(f"Model shape: {self.face_swapper.get_input_shape() if hasattr(self.face_swapper, 'get_input_shape') else 'Unknown'}")
            
            # Initialize tracking variables
            self.face_cache = {}
            self.cache_size = 5
            self.last_detection = None
            self.detection_threshold = 0.3
            self.similarity_threshold = 0.1
            self.debug_mode = True
            
            print("FaceProcessor initialization complete")
            
        except Exception as e:
            print(f"Error initializing FaceProcessor: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

    def set_face_mappings(self, mappings: Dict[str, Any]) -> None:
        """Update the face mappings dictionary with validation"""
        print("\nSetting face mappings:")
        self.face_mappings = {}
        
        for mapping_id, mapping in mappings.items():
            print(f"\nValidating mapping {mapping_id}:")
            if 'source_face' in mapping and mapping['source_face'] is not None:
                source_face = mapping['source_face']
                if 'face' in source_face and 'embedding' in source_face:
                    print("- Source face complete with embedding")
                    print(f"- Embedding shape: {source_face['embedding'].shape}")
                    print(f"- Embedding norm: {np.linalg.norm(source_face['embedding'])}")
                    self.face_mappings[mapping_id] = mapping
                else:
                    print("- Source face missing face or embedding data")
            else:
                print("- No source face data")
                
        print(f"\nTotal valid mappings: {len(self.face_mappings)}")
        
    def detect_faces(self, frame: np.ndarray) -> List[dict]:
        """Detect and analyze faces in a frame"""
        if frame is None:
            print("Frame is None")
            return []
                
        try:
            print(f"Frame shape: {frame.shape}")
            print(f"Frame dtype: {frame.dtype}")
            print("Attempting face detection...")
            faces = self.face_analyzer.get(frame)
            print(f"Detected {len(faces)} faces")
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
        
    def find_best_match(self, target_embedding: np.ndarray) -> Optional[Dict[str, Any]]:
        """Find the best matching source face for a target embedding"""
        try:
            if not self.face_mappings:
                print("No face mappings available")
                return None
            
            best_match = None
            best_similarity = self.similarity_threshold
            
            # Preprocess target embedding
            target_embedding = self.preprocess_embedding(target_embedding)
            print(f"\nProcessed target embedding - mean: {np.mean(target_embedding):.3f}, std: {np.std(target_embedding):.3f}")
            
            for mapping_id, mapping in self.face_mappings.items():
                if 'source_face' not in mapping or mapping['source_face'] is None:
                    continue
                
                source_face = mapping['source_face']
                if 'embedding' not in source_face:
                    continue
                
                # Preprocess source embedding
                source_embedding = self.preprocess_embedding(source_face['embedding'])
                print(f"Processed source embedding - mean: {np.mean(source_embedding):.3f}, std: {np.std(source_embedding):.3f}")
                
                # Calculate cosine similarity
                similarity = float(np.dot(target_embedding, source_embedding))
                print(f"Raw similarity score: {similarity:.3f}")
                
                # Additional similarity metrics
                l2_dist = np.linalg.norm(target_embedding - source_embedding)
                print(f"L2 distance: {l2_dist:.3f}")
                
                # Adjust similarity score
                adjusted_similarity = (1.0 - l2_dist/2.0) * similarity
                print(f"Adjusted similarity score: {adjusted_similarity:.3f}")
                
                if adjusted_similarity > best_similarity:
                    best_similarity = adjusted_similarity
                    best_match = {
                        'mapping_id': mapping_id,
                        'source_face': source_face['face'],
                        'similarity': adjusted_similarity
                    }
            
            if best_match:
                print(f"\nFound match with similarity: {best_similarity:.3f}")
            else:
                print(f"\nNo match found above threshold ({self.similarity_threshold})")
            
            return best_match
        
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

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        if frame is None:
            return frame
        
        try:
            result = frame.copy()
            current_faces = self.detect_faces(frame)
            
            if not current_faces:
                return frame
            
            # Only draw detection boxes if debug mode is enabled
            if self.debug_mode:
                for face in current_faces:
                    x1, y1, x2, y2 = map(int, face['bbox'])
                    cv2.rectangle(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            swapped = result.copy()
            swap_successful = False
            
            for face in current_faces:
                match = self.find_best_match(face['embedding'])
                if match:
                    try:
                        swapped = self.face_swapper.get(
                            swapped,
                            face['face'],
                            match['source_face'],
                            paste_back=True
                        )
                        swap_successful = True
                        
                        # Draw swap indicator if debug mode is enabled
                        if self.debug_mode:
                            x1, y1 = map(int, face['bbox'][:2])
                            cv2.putText(
                                swapped,
                                f"Swapped ({match['similarity']:.2f})",
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5,
                                (0, 255, 0),
                                2
                            )
                    except Exception as e:
                        print(f"Error in face swap: {e}")
                        continue
                    
            return swapped if swap_successful else result
            
        except Exception as e:
            print(f"Error in process_frame: {e}")
            return frame

    def extract_face(self, frame: np.ndarray, bbox) -> Optional[np.ndarray]:
        """Extract face region from frame"""
        try:
            x1, y1, x2, y2 = map(int, bbox)
            return frame[y1:y2, x1:x2]
        except Exception as e:
            print(f"Error extracting face: {str(e)}")
            return None
        
    def analyze_face(self, frame: np.ndarray) -> Optional[Dict[str, Any]]:
        """Analyze a face in an image with detailed debugging"""
        print("\nAnalyzing source face image...")
        
        faces = self.detect_faces(frame)
        if not faces:
            print("No faces detected in source image")
            return None
        
        print(f"Detected {len(faces)} faces in source image")
        face_data = faces[0]  # Get the first detected face
        
        # Debug face data
        print("\nFace data details:")
        print(f"- Bounding box: {face_data['bbox']}")
        print(f"- Embedding shape: {face_data['embedding'].shape}")
        print(f"- Embedding norm: {np.linalg.norm(face_data['embedding'])}")
        print(f"- Embedding min/max: {face_data['embedding'].min():.3f}/{face_data['embedding'].max():.3f}")
        
        # Extract face region
        face_img = self.extract_face(frame, face_data['bbox'])
        
        if face_img is not None:
            result = {
                'face': face_data['face'],
                'embedding': face_data['embedding'],
                'image': face_img
            }
            print("Face analysis complete - data extracted successfully")
            return result
        else:
            print("Failed to extract face image")
            return None

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

    def preprocess_embedding(self, embedding: np.ndarray) -> np.ndarray:
        """Preprocess face embedding for better matching"""
        # Ensure embedding is float32
        embedding = embedding.astype(np.float32)
        
        # L2 normalization
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
            
        # Optional: Zero mean
        embedding = embedding - np.mean(embedding)
        
        return embedding

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

def preprocess_celebrities(face_processor, images_dir):
    """Preprocess celebrity images and return mappings for the gallery."""
    import os
    import cv2

    def load_celebrity_images(images_dir):
        """Load celebrity images from the specified directory."""
        celebrities = {}
        for celebrity in os.listdir(images_dir):
            celebrity_dir = os.path.join(images_dir, celebrity)
            if os.path.isdir(celebrity_dir):
                # Collect all images in the celebrity's directory
                images = [
                    os.path.join(celebrity_dir, file)
                    for file in os.listdir(celebrity_dir)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg'))
                ]
                if images:
                    celebrities[celebrity] = images
        return celebrities

    celebrity_images = load_celebrity_images(images_dir)
    predefined_faces = {}

    for celebrity, images in celebrity_images.items():
        # Use the first image for gallery display
        preview_image = images[0]
        preview_data = face_processor.analyze_face(cv2.imread(preview_image))

        if preview_data:
            predefined_faces[celebrity] = {
                "image": preview_image,
                "embedding": preview_data['embedding'],
            }

    return predefined_faces
