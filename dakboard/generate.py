import os
import dotw
import week

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
    """Generates the time on the top image"""
    pass

def generate_date():
    """Generates the date on the top image"""
    pass

def generate_temperature():
    """Generates the temperature on the top image"""
    pass

def generate_weather_icon():
    """Generates the weather icon on the top image"""
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

    # Generate Sample week
    sample_day = [{
        "type" : "all_day",
        "description" : "All day event"
    },{
        "type" : "scheduled",
        "start_time" : "10:00",
        "description" : "Dentist Appointment"
    },{
        "type" : "scheduled",
        "start_time" : "13:00",
        "description" : "Very long text that will take more than one line to adequately describe, so much text!"
    }]
    b = week.generate_day(sample_day)
    c = week.generate_day(sample_day, minimal=True)

    # Generate a Full Week
    new_week = [b] * 3 + [c] * 4
    d = week.generate_week(new_week)
    a.paste(d, (0, 720 + 140 + first_week.size[1]))

    a.save("result.jpg")
