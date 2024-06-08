from PIL import Image
import os

def convert_png_to_jpg(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".png"):
                print(f"Converting {filepath} to JPG format.")
                img = Image.open(filepath)
                rgb_img = img.convert('RGB')  # Convert any transparency to RGB
                jpg_path = filepath[:-4] + '.jpg'
                rgb_img.save(jpg_path, quality=95)  # Save as JPG
                os.remove(filepath)  # Remove the original PNG file
                print(f"Converted and removed {filepath}")

# Specify your dataset directory
DATA_DIRECTORY = r'C:\\Users\\cikku\\Documents\\ThesisPrototype\\dataset'
convert_png_to_jpg(DATA_DIRECTORY)
