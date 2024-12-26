import os
import subprocess

def convert_webp_to_jpg(input_dir):
    """
    Traverse directories starting from input_dir and convert all .webp files to .jpg using ffmpeg.

    Args:
        input_dir (str): The root directory to start the search.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = os.path.join(root, file)
                jpg_path = os.path.splitext(webp_path)[0] + ".jpg"
                
                try:
                    # Convert webp to jpg using ffmpeg
                    subprocess.run([
                        "ffmpeg", "-i", webp_path, jpg_path
                    ], check=True)

                    print(f"Converted: {webp_path} -> {jpg_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {webp_path}: {e}")

if __name__ == "__main__":
    # Replace 'input_directory_path' with the path to the directory containing .webp files
    input_directory_path = "./images"
    convert_webp_to_jpg(input_directory_path)

