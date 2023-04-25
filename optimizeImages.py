from PIL import Image
import os

# Set the desired maximum dimensions for the images
MAX_WIDTH = 1000
MAX_HEIGHT = 1000

# Set the compression quality for JPEG images
JPEG_QUALITY = 90

# Set the compression quality for WebP images
WEBP_QUALITY = 90

# Set the directory where the images are located
input_dir = "/Users/rougeboy/Documents/repos/rougeboy.github.io/photography"

# Set the directory where the optimized images will be saved
output_dir = "/Users/rougeboy/Documents/repos/rougeboy.github.io/test-folder"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each image file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG"):
        # Open the image file
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Calculate the new dimensions for the image
            width, height = img.size
            if width > MAX_WIDTH:
                ratio = MAX_WIDTH / width
                height = int(height * ratio)
                width = MAX_WIDTH
            if height > MAX_HEIGHT:
                ratio = MAX_HEIGHT / height
                width = int(width * ratio)
                height = MAX_HEIGHT
            
            # Resize the image while maintaining aspect ratio
            img.thumbnail((width, height), resample=Image.LANCZOS)
            
            # Save the optimized JPEG image
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path, optimize=True, quality=JPEG_QUALITY, progressive=True)
            
            # Save the optimized WebP image
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path, optimize=True, quality=WEBP_QUALITY)
