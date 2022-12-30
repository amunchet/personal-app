#!/usr/bin/env python3
"""
Generates Details for a given day
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def all_day_event():
    """
    Generates an all day event
        - Will have a colored background, white text
    """

def individual_event(text, font="Lato-Light.ttf"):
    """
    Draws an event
        - Orange dot (variable color)
        - Time 
        - Text (will need to wrap to second line)
        - Colors (will be grey if previous day)
    """
    max_width = 20
    line_height = 25

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
    
    image = Image.new('RGB', (160, (len(lines) * line_height)), (0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the font
    font_path = os.path.join("fonts", font)
    font = ImageFont.truetype(font_path, size=15)

    # Draw the orange dot at the start of the image
    dot_size = 10
    x = 10
    y = 14
    draw.ellipse(
        (x, y, x + dot_size, y + dot_size), 
        fill="green"
    )


    
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

if __name__ == "__main__":

    text = "10:45a Something that takes a very large amount of text to describe it"
    a = individual_event(text)
    a.save("individual-event.jpg")