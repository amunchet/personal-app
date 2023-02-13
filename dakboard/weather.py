import os
import requests
from dakboard_logger import logger
from dotenv import load_dotenv

load_dotenv()

if os.path.exists(".env.sample"):
    load_dotenv(".env.sample")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("WEATHER_API_KEY")
zipcode = os.getenv("WEATHER_ZIPCODE")

if not api_key:
    raise Exception("No Weather key set")


def get_current_weather():
    complete_url = base_url + "appid=" + api_key + "&zip=" + zipcode + ",us"

    response = requests.get(complete_url)
    weather_data = response.json()

    if response.status_code == 200:
        return weather_data['weather'][0]['main']
    else:
        logger.error(response.text)
        return None

def get_current_temperature():
    complete_url = base_url + "appid=" + api_key + "&zip=" + zipcode + ",us"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        temperature_C = data["main"]["temp"] - 273.15
        temperature_F = (temperature_C * 9/5) + 32
        return temperature_F
    else:
        return "Invalid zip code."
