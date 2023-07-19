import os
from PIL import Image

def cut_image_into_segments(folder_path, output_folder):
    image_files = os.listdir(folder_path)

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        if not os.path.isfile(image_path):
            continue

        image = Image.open(image_path)
        width, height = image.size
        segment_height = height // 2

        for i in range(2):
            top = i * segment_height
            bottom = top + segment_height
            segment = image.crop((0, top, width, bottom))

            segment_filename = f"{image_file}_{i+1}.jpg" or f"{image_file}_{i+1}.png"
            segment_save_path = os.path.join(output_folder, segment_filename)
            segment.save(segment_save_path)

            print(f"Segment {i+1} of {image_file} saved as {segment_filename}")

# Example usage
input_folder = r"C:\Users\Racha\OneDrive\Desktop\Test"
output_folder = r"C:\Users\Racha\OneDrive\Desktop\Test"

cut_image_into_segments(input_folder, output_folder)
