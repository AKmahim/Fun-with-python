# ==================================== add background to all alpona ====================================

import os
from PIL import Image

# Path to the folder containing PNG images
folder_path = "alpona/"

# Path to the background image
background_image_path = "canvas-bg.jpg"

# Create a folder to store output images
output_folder = "alpona-with-bg2"
os.makedirs(output_folder, exist_ok=True)

# Open the background image
background_image = Image.open(background_image_path)

# Get the size of the background image
background_width, background_height = background_image.size

# Iterate through all PNG images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # Open the PNG image
        png_image_path = os.path.join(folder_path, filename)
        png_image = Image.open(png_image_path)

        # Calculate the position to place the PNG image in the middle of the background image
        x_offset = (background_width - png_image.width) // 2
        y_offset = (background_height - png_image.height) // 2

        # Create a new image with the same size as the background image and paste the PNG image onto it
        composed_image = background_image.copy()
        composed_image.paste(png_image, (x_offset, y_offset), png_image)

        # Save the composed image in the output folder with the same filename
        output_path = os.path.join(output_folder, filename.replace(".png", "_with_background.png"))
        composed_image.save(output_path)

        print(f"Background added to {filename} and saved as {output_path}")

print("Background added to all PNG images.")















# ======================================== with plain background =========================== 

# import os
# from PIL import Image

# # Path to the folder containing PNG images
# folder_path = "alpona/"

# # Background color (in RGB format)
# background_color = (45, 46, 46)

# # Create a folder to store output images
# output_folder = "alpona-with-plain-bg"
# os.makedirs(output_folder, exist_ok=True)

# # Iterate through all PNG images in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".png"):
#         # Open the PNG image
#         png_image_path = os.path.join(folder_path, filename)
#         png_image = Image.open(png_image_path)

#         # Create a new image with the same size as the PNG image and fill it with the background color
#         background_image = Image.new("RGB", png_image.size, background_color)

#         # Composite the PNG image onto the background image
#         composed_image = Image.alpha_composite(background_image.convert("RGBA"), png_image.convert("RGBA"))

#         # Save the composed image in the output folder with the same filename
#         output_path = os.path.join(output_folder, filename)
#         composed_image.save(output_path)

#         print(f"Background added to {filename} and saved as {output_path}")

# print("Background added to all PNG images.")
