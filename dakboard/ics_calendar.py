import json
import os
import glob


import datetime

from datetime import datetime, timedelta

import requests
import ics
import pytz
import arrow

import dateutil.rrule as rrule

from dakboard_logger import logger
from dotenv import load_dotenv

load_dotenv()

if os.path.exists(".env.sample"):
    load_dotenv(".env.sample")

TZ = os.getenv("TZ")

def load_calendars():
    """
    Load full ICS calendars
        - Will be passed into parse_events to sort out the events
    """
    if not os.path.exists("calendar.json"):
        raise Exception("No Calendar.json file found - calendar would be empty")

    with open("calendar.json") as f:
        calendars = json.load(f)
        for calendar in calendars:
            logger.debug(f"Calendar {calendar['name']}")
            url = calendar["link"]
            response = requests.get(url)
            if response.status_code != 200:
                logger.error(f"Calendar failed to load: {calendar['name']}")
            events = ics.Calendar(response.text)
            calendar["events"] = events.events

        logger.debug(f"[load_calendars] {calendars}")
        return calendars



def check_recurring(event, start_date, end_date):
    """
    Checks for recurring dates
    """
    tz = pytz.timezone(TZ)   
        
    #start_date = start_date.astimezone(pytz.utc)
    # end_date = end_date.astimezone(pytz.utc)


    retval = False
    for extra in event.extra:
        if "rrule" in str(extra).lower():
            logger.debug(f"[rrule] {event.description}")
            logger.debug(f"[rrule] {event.name}")
            logger.debug("[rrule] Found a rrule")
            logger.debug(f"[rrule] {extra}")
            
            found = rrule.rrulestr(str(extra), dtstart=event.begin, ignoretz=True)
            logger.debug(f"[rrule] {found}")

            try:
                a = found.between(end_date, start_date, inc=True)
            except TypeError:
                start_date = start_date.replace(tzinfo=None)
                end_date = end_date.replace(tzinfo=None)
                found = found.replace(dtstart=event.begin.replace(tzinfo=None))

                a = found.between(start_date, end_date, inc=True)
           
            logger.debug(f"[rrule] Start date: {start_date}")
            logger.debug(f"[rrule] End date: {end_date}")
            logger.debug(f"[rrule] Result of found: {a}")
            if a:
                retval = True

    return retval


def load_events(start_date, calendars):
    """
    Loads all events from the calendars for the given day and the given date + 1 day
    """
    tz = pytz.timezone(TZ)

    if type(start_date) == str:
        start_date = datetime.strptime(start_date,"%Y-%m-%d")
        start_date = tz.localize(start_date)
    
    logger.debug(f"Load events start date: {start_date}")

    # end_date = start_date + timedelta(days=1, minutes=1)
    end_date = start_date + timedelta(hours=23, minutes=59, seconds=59)

    retval = []

    for calendar in calendars:
        logger.debug(f"Calendar {calendar['name']}")
        logger.debug(f"Calendar data:{calendar}")
        for event in calendar["events"]:

            if(
                    (event.begin.datetime >= start_date and event.end.datetime <= end_date) 
                    or (event.all_day and event.begin.date() == arrow.get(start_date).date()
                    or check_recurring(event, start_date, end_date)
            )):

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
