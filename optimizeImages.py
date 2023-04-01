from PIL import Image
import os

# Set the maximum width and height of the optimized images
max_size = (500, 750)

# Set the quality level for the optimized images
quality = 80

# Set the directory where the original images are located
input_dir = "/Users/rougeboy/Documents/repos/Portfolio/jpeg-optimized"

# Set the directory where the optimized images will be saved
output_dir = "/Users/rougeboy/Documents/repos/Portfolio/jpeg-optimized"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Open the original image
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Resize the image to fit within the maximum size
            img.thumbnail(max_size, Image.ANTIALIAS)
            # Save the optimized image to the output directory
            img.save(os.path.join(output_dir, filename), optimize=True, quality=quality)

# Print the file name and the percentage of space saved
before_size = os.path.getsize(os.path.join(input_dir, filename))
after_size = os.path.getsize(os.path.join(output_dir, filename))
saved_percent = round((before_size - after_size) / before_size * 100, 2)
print(f"{filename} optimized ({saved_percent}% space saved)")