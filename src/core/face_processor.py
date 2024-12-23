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
        """Initialize face processing components with enhanced quality settings"""
        try:
            print("\nInitializing FaceProcessor...")
            self.face_mappings = {}
            self.models_dir = self._get_models_dir()
            self.execution_provider = self._get_execution_provider()
            
            # Initialize face analyzer with higher resolution
            print("Loading face analyzer...")
            self.face_analyzer = FaceAnalysis(
                name='buffalo_l',
                providers=[self.execution_provider],
                allowed_modules=['detection', 'recognition']
            )
            # Increase detection size for better quality
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
            self.similarity_threshold = 0.2  # Lower threshold for better matching
            self.cache_size = 10  # Increased cache size
            self.process_every_n_frames = 1  # Process every frame
            
            # Face detection settings
            self.detection_threshold = 0.6  # Increased confidence threshold
            self.min_face_size = 30  # Minimum face size to process
            
            # Image enhancement settings
            self.use_face_enhancement = True
            self.enhancement_level = 1.0  # Adjustable enhancement strength
            
            print("FaceProcessor initialization complete with enhanced settings")
            
        except Exception as e:
            print(f"Error initializing FaceProcessor: {str(e)}")
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
            
            for mapping_id, mapping in self.face_mappings.items():
                if 'source_face' not in mapping:
                    continue
                    
                source_data = mapping['source_face']
                
                # Check if we have multiple embeddings
                if 'all_embeddings' in source_data:
                    # Compare with each embedding
                    similarities = []
                    for idx, emb in enumerate(source_data['all_embeddings']):
                        source_embedding = self.preprocess_embedding(emb)
                        similarity = float(np.dot(target_embedding, source_embedding))
                        l2_dist = np.linalg.norm(target_embedding - source_embedding)
                        adjusted_similarity = (1.0 - l2_dist/2.0) * similarity
                        similarities.append((adjusted_similarity, idx))
                    
                    # Get the best matching face
                    if similarities:
                        best_local_similarity, best_idx = max(similarities)
                        if best_local_similarity > best_similarity:
                            best_similarity = best_local_similarity
                            best_match = {
                                'mapping_id': mapping_id,
                                'source_face': source_data['all_faces'][best_idx],
                                'similarity': best_local_similarity
                            }
                else:
                    # Fall back to single embedding comparison
                    if 'embedding' not in source_data:
                        continue
                        
                    source_embedding = self.preprocess_embedding(source_data['embedding'])
                    similarity = float(np.dot(target_embedding, source_embedding))
                    l2_dist = np.linalg.norm(target_embedding - source_embedding)
                    adjusted_similarity = (1.0 - l2_dist/2.0) * similarity
                    
                    if adjusted_similarity > best_similarity:
                        best_similarity = adjusted_similarity
                        best_match = {
                            'mapping_id': mapping_id,
                            'source_face': source_data['face'],
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

    def process_frame(self, frame):
        """Process frame with enhanced quality settings"""
        if frame is None:
            return frame
        
        try:
            result = frame.copy()
            current_faces = self.detect_faces(frame)
            
            if not current_faces:
                return frame
            
            swapped = result.copy()
            swap_successful = False
            
            for face in current_faces:
                # Skip small faces
                bbox_width = face['bbox'][2] - face['bbox'][0]
                if bbox_width < self.min_face_size:
                    continue
                    
                match = self.find_best_match(face['embedding'])
                if match and match['similarity'] > self.similarity_threshold:
                    try:
                        # Apply face swap with enhanced settings
                        swapped = self.face_swapper.get(
                            swapped,
                            face['face'],
                            match['source_face'],
                            paste_back=True
                        )
                        
                        # Apply face enhancement if enabled
                        if self.use_face_enhancement:
                            swapped = self.enhance_face_region(
                                swapped,
                                face['bbox'],
                                self.enhancement_level
                            )
                            
                        swap_successful = True
                        
                        # Draw swap indicator if debug mode is enabled
                        if self.debug_mode:
                            x1, y1, x2, y2 = map(int, face['bbox'])
                            cv2.rectangle(swapped, (x1, y1), (x2, y2), (0, 255, 0), 2)
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
