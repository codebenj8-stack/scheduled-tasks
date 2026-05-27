import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    # "lat": 53.410782,
    # "lon": -2.977840,
    "lat": 55.755825,
    "lon": 37.617298,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

twelve_hr_id_list = [weather_data["list"][index]["weather"][0]["id"] for index in range(4)]
will_rain = False
for id in twelve_hr_id_list:
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an ☔",
        from_ = "whatsapp:+14155238886",
        to = "whatsapp:+447464638564",
    )
    print(message.status)

