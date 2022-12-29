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



if __name__ == "__main__":
    a = create_image_combine_top(os.path.join("design", "test-top.png"))

    dotw_header = dotw.dotw_header()

    a.paste(dotw_header, (0, 720))


    a.save("result.jpg")
