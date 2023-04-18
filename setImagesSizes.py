from PIL import Image
import os

# set the directory where your images are stored
input_folder = "/Users/rougeboy/Documents/repos/Portfolio/jpeg-optimized"
output_folder = "/Users/rougeboy/Documents/repos/Portfolio/resized-images"

def resize_images_by_width(input_folder, output_folder, width):
    """Resizes all images in a folder by width and saves them to a new folder"""
    for filename in os.listdir(input_folder):
        try:
            # Check if the file is a JPEG image
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".JPG"):
                # Open the image
                with Image.open(os.path.join(input_folder, filename)) as image:
                    # Resize by width
                    wpercent = (width / float(image.size[0]))
                    hsize = int((float(image.size[1]) * float(wpercent)))
                    resized_image = image.resize((width, hsize), Image.ANTIALIAS)
                    
                    # Save the resized image
                    resized_image.save(os.path.join(output_folder, filename))
                    
        except IOError:
            print("Cannot resize image {}".format(filename))

# Example usage
width = 800

resize_images_by_width(input_folder, output_folder, width)
