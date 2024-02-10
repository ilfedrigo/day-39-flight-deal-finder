import requests
import json
from datetime import datetime, timedelta

today_date = datetime.now().strftime("%d/%m/%Y")

SHEET_ENDPOINT = "https://api.sheety.co/2562639edf04f0d34bec0ec17a4b4386/flightDeals/prices"
FLIGHTS_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

today_date_dt = datetime.strptime(today_date, "%d/%m/%Y")

six_months_later = today_date_dt + timedelta(days=30*6)

today_date_str = today_date_dt.strftime("%d/%m/%Y")
flight_until_str = six_months_later.strftime("%d/%m/%Y")

headers = {
    "apikey": "XrGbMKv234wykN5jTgV6LtRgmaMpJug4",
}

parameters = {
    "fly_from": "DUB",
    "fly_to": "NRT",
    "date_from": today_date_str,
    "date_to": flight_until_str,
}

response = requests.get(FLIGHTS_ENDPOINT, params=parameters, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open("flights_data_json", "w") as file:
        file.write(json.dumps(data, indent=4))