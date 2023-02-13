import os
import datetime

import dotw
import week
import weather

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

def generate_time(im, now=None):
    """Generates the time on the top image"""
    # Create a draw object that can be used to draw on the image
    draw = ImageDraw.Draw(im)

    if not now:
        # Get the current time
        now = datetime.datetime.now().time()

        # Format the current time as a string in the desired format (HH:MM)
        time_str = now.strftime("%H:%M")
    else:
        time_str = now

    # Specify the font and font size to use
    font = ImageFont.truetype("arial.ttf", 50)

    # Get the size of the text
    text_size = draw.textsize(time_str, font)

    # Calculate the position to draw the text on the image
    x = 20
    # y = im.height - text_size[1]
    y = 600

    # Draw the text on the image
    draw.text((x, y), time_str, font=font, fill=(255, 255, 255))

    return im

def generate_date(im, date_str=None):
    """Generates the date on the top image"""
    # Create a draw object that can be used to draw on the image
    draw = ImageDraw.Draw(im)

    if not date_str:
        # Get the current date and time
        now = datetime.datetime.now()
        # Format the current date and day as a string in the desired format (Wednesday, May 31)
        date_str = now.strftime("%A, %B %d")

    # Specify the font and font size to use
    font = ImageFont.truetype("arial.ttf", 30)

    # Get the size of the text
    text_size = draw.textsize(date_str, font)

    # Calculate the position to draw the text on the image
    x = 25
    # y = im.height - text_size[1]
    y = 660

    # Draw the text on the image
    draw.text((x, y), date_str, font=font, fill=(255, 255, 255))

    # Save the modified image
    return im

def generate_temperature(image, temperature):
    """Generates the temperature on the top image"""
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 60)
    text = f"{temperature:.0f}°"
    text_width, text_height = draw.textsize(text, font)
    x = image.width - text_width - 10
    y = 630
    color = (0,0,0)
    draw.text((x, y), text, font=font, fill=color)
    return image

def generate_weather_icon(base_image, weather_condition):
    """Generates the weather icon on the top image"""
    path = os.path.join("images", "weather")
    weather_icons = {
        'Clear': 'icons8-sun-100.png',
        'Clouds': 'icons8-icloud-100.png',
        'Rain': 'icons8-rain-100.png',
        'Thunderstorm': 'icons8-cloud-lightning-100.png',
        'Snow': 'icons8-snow-100.png',
        'Mist': 'icons8-fog-100.png',
        'Drizzle': 'icons8-rain-100.png',
        'Haze': 'icons8-fog-100.png',
        'Fog': 'icons8-fog-100.png',
        'Sand': 'icons8-fog-100.png',
        'Dust': 'icons8-fog-100.png',
        'Ash': 'icons8-fog-100.png',
        'Squall': 'icons8-cloud-lightning-100.png',
        'Tornado': 'icons8-tornado-100.png'
    }
    for item in weather_icons:
        weather_icons[item] = os.path.join(path, weather_icons[item])

    icon = Image.open(weather_icons.get(weather_condition, 'icons8-sun-100.png'))
    icon_width, icon_height = icon.size
    base_image.paste(
        icon, 
        (
            base_image.width - icon_width - 10, 
            # 0,
            # base_image.height - icon_height), 
            550), 
        icon
    )

    return base_image

if __name__ == "__main__": # pragma: no cover
    # Generate base and top image
    a = create_image_combine_top(os.path.join("photos", "test-top-edit.png"))

    # Get weather and temperature
    ## Put onto top image
    a = generate_time(a, "11:04")
    a = generate_date(a, "Wednesday, May 31")

    # Get time and date
    ## Put onto top image
    a = generate_temperature(a, 90)
    a = generate_weather_icon(a, "Clouds")

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
        "description" : "All day event",
        "color" : "red"
    },{
        "type" : "scheduled",
        "start_time" : "10:00",
        "description" : "Dentist Appointment",
        "color" : "orange"
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
