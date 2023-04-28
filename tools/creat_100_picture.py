from PIL import Image

def crop_to_square(image):
    # Get the size of the input image
    width, height = image.size
    # Determine the shorter side length
    cropped_size = min(width, height)
    # Calculate the cropping box
    left = (width - cropped_size) // 2
    upper = (height - cropped_size) // 2
    right = left + cropped_size
    lower = upper + cropped_size
    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))
    return cropped_image

def change_background_color(image, color):
    # Create a new image with the desired background color
    background = Image.new(image.mode, image.size, color)
    # Combine the background image and the original image using alpha composite
    result = Image.alpha_composite(background, image)
    return result

# Load an image
input_image = Image.open("脊骨11.png")
# Crop the image to a square
cropped_image = crop_to_square(input_image)
# Resize the image to a smaller size
resized_image = cropped_image.resize((100, 100))
# Change the background color to red
output_image = change_background_color(resized_image, (255,255,225,0))
# Save the output image
output_image.save("output_image.png")