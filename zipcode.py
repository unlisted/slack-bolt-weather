import os
from pprint import pprint
import requests

ZIPCODE_API_KEY = os.getenv("ZIPCODE_API_KEY")

def get_location_from_zipcode(zipcode):
    assert zipcode is not None
    assert ZIPCODE_API_KEY is not None

    units = "degrees"
    frmat = "json"
    url = f"https://www.zipcodeapi.com/rest/{ZIPCODE_API_KEY}/info.{frmat}/{zipcode}/{units}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    location = get_location_from_zipcode("07030")
    pprint(location)