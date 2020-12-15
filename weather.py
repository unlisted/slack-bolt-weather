import requests

def get_weather_for_zipcode(zipcode, api_key):
    assert zipcode is not None
    assert api_key is not None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={zipcode},US&APPID={api_key}"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


