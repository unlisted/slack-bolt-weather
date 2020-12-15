import requests

def get_location_from_zipcode(zipcode, api_key):
    assert zipcode is not None
    assert api_key is not None

    units = "degrees"
    frmat = "json"
    url = f"https://www.zipcodeapi.com/rest/{api_key}/info.{frmat}/{zipcode}/{units}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()
