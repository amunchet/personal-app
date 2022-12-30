import os
import dotw

from PIL import Image, ImageDraw, ImageFont
def create_image_combine_top(top_image, width=1080, height=1920):
    """
    Creates a canvas and puts the image on it
    """

    # Open the image from the specified path
    top_image = Image.open(top_image)

    # Create a blank image with the desired size
    bottom_image = Image.new('RGB', (width, height), 'black')

    # Paste the top image onto the bottom image
    bottom_image.paste(top_image, (0, 0))

    # Save the resulting image
    return bottom_image

def generate_time():
    pass

def generate_date():
    pass

def generate_temperature():
    pass

def generate_weather_icon():
    pass


if __name__ == "__main__":
    a = create_image_combine_top(os.path.join("design", "test-top.png"))

    dotw_header = dotw.dotw_header()
    a.paste(dotw_header, (0, 720))

    items = [
        ("28", False),
        ("29", False),
        ("30", False),
        ("31", True),
        ("Jun", False),
        ("2", False),
        ("3", False)
    ]
    first_week = dotw.dotw_header(items)

    a.paste(first_week, (0, 720 + 140))

    a.save("result.jpg")
