import os
from PIL import Image, ImageDraw, ImageFont

def dotw_item(letter, font_name="Lato-Bold.ttf", font_size=55):
    """
    Creates the image for the day of the week header
    """
    font_location = os.path.join("fonts", font_name)
    # Create a blank image with the desired size and background color
    image = Image.new('RGB', (154, 140), (0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the custom font
    font = ImageFont.truetype(font_location, size=font_size)

    # Calculate the position of the center of the image
    center_x = image.width // 2
    center_y = image.height // 2 - (font_size // 4)

    # Draw the letter in the center of the image using the custom font
    text_w, text_h = draw.textsize(letter, font=font)
    draw.text((center_x - text_w // 2, center_y - text_h // 2), letter, font=font, fill=(255, 255, 255))

    # Save the resulting image
    return image

def dotw_header():
    """
    Creates the header row for the days of the week
    """
    letters = "SMTWTFS"
    images = [dotw_item(letter) for letter in letters]

    total_width = sum(image.width for image in images)

    # Create a blank image with the desired size
    result = Image.new('RGB', (total_width, max(image.height for image in images)))

    # Paste the images onto the blank image
    x_offset = 1
    for image in images:
        result.paste(image, (x_offset, 0))
        x_offset += image.width

    # Save the resulting image
    return result

if __name__ == "__main__":

    b = dotw_header()
    b.save("font-header-test.jpg")