import os
from PIL import Image

# Set the path for the working and output directories
working_dir = "./working/"
output_dir = "./output/"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all the .jpg files in the working directory
for filename in os.listdir(working_dir):
    if filename.endswith(".jpg"):
        # Open the image with Pillow
        img = Image.open(os.path.join(working_dir, filename))
        
        # Reduce the image size to 20% of its original dimensions
        new_size = tuple(int(x*0.2) for x in img.size)
        resized_img = img.resize(new_size)
        
        # Save the resized image to the output directory
        resized_img.save(os.path.join(output_dir, filename))