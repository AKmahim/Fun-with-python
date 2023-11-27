from PIL import Image

# Open the uploaded image
image = Image.open('test.jpg')

# Define the wall region (coordinates or segmentation)

# Define the new wall color
new_color = (255, 0, 0)  # Red in RGB format

# Replace the color in the wall region
for x in range(region_x_start, region_x_end):
    for y in range(region_y_start, region_y_end):
        image.putpixel((x, y), new_color)

# Save the modified image
image.save('uploads/modified_image.jpg')

# You would then serve the modified image to the user
