#!/usr/bin/env python3
"""
Generates Details for a given day
"""
import os
import textwrap
from typing import List
from PIL import Image, ImageDraw, ImageFont
from dakboard_logger import logger

def individual_event(text, font="Lato-Light.ttf", all_day=False):
    """
    Draws an event
        - Orange dot (variable color)
        - Time
        - Text (will need to wrap to second line)
        - Colors (will be grey if previous day)

    Can be `all_day`, which means
        - No orange dot
        - colored background
        - white text
    """
    max_width = 20
    line_height = 28
    radius = 12
    day_width = 155

    # Split the text into lines that fit within the maximum width
    temp = text.split(" ")

    lines = []
    line = ""
    for item in temp:
        if len(item) + len(line) > max_width:
            lines.append(line)
            line = ""
        line += item + " "

    if line != "":
        lines.append(line)

    # Create a blank image with the desired size and background color

    image = Image.new("RGB", (day_width, (len(lines) * line_height) + 5), (0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # If we are an all day event, create the rectangle
    if all_day:
        calc_line_height = (len(lines) * line_height) - 10

        if calc_line_height < line_height:
            calc_line_height = line_height
        rectangle = [(10, 10), (day_width- 10, calc_line_height)]
        draw.rounded_rectangle(rectangle, fill=(255, 0, 0), radius=radius)

    # Load the font
    font_path = os.path.join("fonts", font)
    font = ImageFont.truetype(font_path, size=15)

    # Draw the orange dot at the start of the image
    dot_size = 10
    x = 10
    y = 14
    if not all_day:
        draw.ellipse((x, y, x + dot_size, y + dot_size), fill="green")

    # Calculate the position of the first line of text
    x = 20
    y = 10

    # Draw the lines of text one by one
    if lines:
        lines[0] = "  " + lines[0]

    for line in lines:
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += font.getsize(line)[1]

    return image

def generate_day(events:List, minimal=False):
    """
    Generates an image based on the events list

    Each events detail format:
        - type: `all_day` or `scheduled`
        - description: self-explanatory
        - start_time [optional] : only used on scheduled
    
    `minimal` - whether or not to squish the events into 1 line
    """

    width = 155

    retval = []
    inner_height = 0

    for item in events:
        logger.debug(f"Event:{item}")

        desc = item["description"]
        if "start_time" in item:
            desc = f"{item['start_time']} {item['description']}"


        if minimal:
            if len(desc) > 20:
                desc = desc[:17] + "..."

        a = individual_event(desc, all_day = item["type"] == "all_day")
        retval.append(a)

        logger.debug(f"Height for this event is: {a.size[1]}")

        inner_height += a.size[1]

        logger.debug(f"Now inner height is {inner_height}")

    logger.debug(f"Inner height:{inner_height}")

    image = Image.new("RGB", (width, inner_height), (0, 0, 0))

    # Create a drawing context
    current_height = 0
    for item in retval:
        logger.debug(f"Current image height:{image.size[1]}")

        image.paste(item, (0, current_height))
        current_height += item.size[1]
        
        logger.debug(f"Current height:{current_height}")
    return image

def generate_week(days):
    """
    Generates a week from an array of day images
    """
    width = 155
    height = max([x.size[1] for x in days])
    
    image = Image.new("RGB", (width * len(days), height), (0, 0, 0))

    for (idx,day) in enumerate(days):
        image.paste(day, (idx * width, 0))
    
    return image



if __name__ == "__main__":
    # Individual Event
    text = "10:45a Something that takes a very large amount of text to describe it"
    a = individual_event(text)
    a.save("individual-event.jpg")

    # All Day
    text = "An all day event that takes a very large amount of text to describe"
    a = individual_event(text, all_day=True)
    a.save("all-day-event.jpg")

    # Generate a Full Day
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
    b = generate_day(sample_day)
    b.save("day.jpg")

    a = generate_day(sample_day, minimal=True)
    a.save("day-minimal.jpg")

    # Generate a Full Week
    week = [a] * 3 + [b] * 4
    c = generate_week(week)
    c.save("week.jpg")
