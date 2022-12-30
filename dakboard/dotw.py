import os
from PIL import Image, ImageDraw, ImageFont

def dotw_item(letter, font_name="Lato-Bold.ttf", font_size=55, width=154, height=140, circle=False):
    """
    Creates the image for the day of the week header
    """
    font_location = os.path.join("fonts", font_name)
    # Create a blank image with the desired size and background color
    image = Image.new('RGB', (width, height), (0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the custom font
    font = ImageFont.truetype(font_location, size=font_size)

    # Calculate the position of the center of the image
    center_x = image.width // 2
    center_y = image.height // 2 - (font_size // 4)

    # Draw the letter in the center of the image using the custom font
    text_w, text_h = draw.textsize(letter, font=font)

    if circle:
        # Calculate the coordinates of the bounding box for the circle
        x1 = center_x - text_w // 2 - 10 
        y1 = center_y - text_h // 2 - 10 + 7
        x2 = center_x + text_w // 2 + 10
        y2 = center_y + text_h // 2 + 10 + 10

        # Draw the circle around the text
        draw.ellipse((x1, y1, x2, y2), fill=(255, 0, 0))
        
        # Outline only
        # draw.arc((x1, y1, x2, y2), 0, 360, fill=(255, 0, 0))

    draw.text((center_x - text_w // 2, center_y - text_h // 2), letter, font=font, fill=(255, 255, 255))

    # Save the resulting image
    return image

def dotw_header(items=""):
    """
    Creates the header row for the days of the week or any other header
        - Needs to account for Month change
        - Will have one item with a circle around it
    """
    if items == "":
        letters = "SMTWTFS"
        images = [dotw_item(letter) for letter in letters]
    else:
        images = [dotw_item(letter, circle=circle) for (letter, circle) in items]

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

    items = [
        ("28", False),
        ("29", False),
        ("30", False),
        ("31", True),
        ("Jun", False),
        ("2", False),
        ("3", False)
    ]
    c = dotw_header(items)
    c.save("sample.jpg")