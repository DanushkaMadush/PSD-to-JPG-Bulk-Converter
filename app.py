import os
from psd_tools import PSDImage
from PIL import Image

# Directory containing the PSD files
input_dir = r"D:\Danushka\python\psd"
output_dir = r"D:\Danushka\python\jpg"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through all PSD files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.lower().endswith('.psd'):
        psd_path = os.path.join(input_dir, file_name)
        psd = PSDImage.open(psd_path)

        # Convert PSD to PIL image
        composite_image = psd.composite()

        # Ensure the image is in RGB mode
        if composite_image.mode == 'RGBA':
            composite_image = composite_image.convert('RGB')

        output_path = os.path.join(output_dir, file_name.replace('.psd', '.jpg'))

        # Save as JPEG
        composite_image.save(output_path, 'JPEG')
        print(f"Converted {file_name} to {output_path}")
