import json
import os
import glob


import datetime

from datetime import datetime, timedelta

import requests
import ics
import pytz
import arrow

from dakboard_logger import logger
from dotenv import load_dotenv

load_dotenv()

if os.path.exists(".env.sample"):
    load_dotenv(".env.sample")

TZ = os.getenv("TZ")

def load_events(start_date):
    """
    Loads all events from the calendars for the given day and the given date + 1 day
    """
    if not os.path.exists("calendar.json"):
        raise Exception("No Calendar.json file found - calendar would be empty")

    tz = pytz.timezone(TZ)

    if type(start_date) == str:
        start_date = datetime.strptime(start_date,"%Y-%m-%d")
        start_date = tz.localize(start_date)
    
    logger.debug(f"Load events start date: {start_date}")

    end_date = start_date + timedelta(days=1, minutes=1)

    with open("calendar.json") as f:
        calendars = json.load(f)
    
    retval = []

    for calendar in calendars:
        logger.debug(f"Calendar {calendar['name']}")
        url = calendar["link"]
        response = requests.get(url)
        if response.status_code != 200:
            logger.error(f"Calendar failed to load: {calendar['name']}")
        events = ics.Calendar(response.text)
        for event in events.events:

            if(event.begin.datetime >= start_date and event.end.datetime <= end_date) or (event.all_day and event.begin.date() == arrow.get(start_date).date()):
                color = (calendar["color"] if "color" in calendar else "")
                event_type = "all_day" if event.all_day else "scheduled"
                start_time = f"{event.begin.hour:02}:{event.begin.minute:02}"
                description = event.name

                output = {
                    "type" : event_type,
                    "description" : description,
                    "color" : color,
                    "start_time" : start_time
                }
                logger.debug(f"Calendar event:{output}")
                retval.append(output)
    logger.debug(f"Calendar retval: {retval}")
    return retval
