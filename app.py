import os
from signal import signal, SIGINT
from sys import exit
from Secret import Secret
from requests.exceptions import HTTPError
from weather import get_weather_for_zipcode
from zipcode import get_location_from_zipcode

from slack_bolt import App

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

SECRET = Secret.get_instance()
app = App(
    token=SECRET.secrets.get("SLACK_BOT_TOKEN"),
    signing_secret=SECRET.secrets.get("SLACK_SIGNING_SECRET")
)
  
@app.command("/weather")
def weather(ack, say, command):
    ack()

    user_id = command.get("user_id")
    prefix = f"Hey <@{user_id}>, "

    zipcode = command.get("text")
    if zipcode is None:
      say(f"{prefix}provide a zipcode.")
      return

    #TODO: input validation

    try:
      weather = get_weather_for_zipcode(zipcode, SECRET.secrets["WEATHER_API_KEY"])
    except HTTPError as e:
      say(f"{prefix}\"{zipcode}\" is not a valid zipcode.")
      return
    
    feels_like_k = weather["main"]["feels_like"]
    feels_like_f = (feels_like_k - 273.15) * 1.8000 + 32.00

    try:
      location = get_location_from_zipcode(zipcode, SECRET.secrets["ZIPCODE_API_KEY"])
    except HTTPError as e:
      message = f"{prefix}It feels like {feels_like_f:.0f} in {zipcode}."
    else:
      city = location["city"]
      state = location["state"]
      message = f"{prefix}It feels like {feels_like_f:.0f} in {city}, {state}."
    
    blocks = {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }
        ]
    }
    say(blocks)

# Start your app
if __name__ == "__main__":
  signal(SIGINT, handler)
  app.start(port=int(os.environ.get("PORT", 3000)))