import json
import os
import requests
from pprint import pprint

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather_for_zipcode(zipcode):
    assert zipcode is not None
    assert WEATHER_API_KEY is not None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={zipcode},US&APPID={WEATHER_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()
if __name__ == "__main__":
    pprint(get_weather_for_zipcode(None))

