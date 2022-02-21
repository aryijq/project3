import requests
import json

API_URL = "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&oneWay=false&nonStop=false"

raw_data = requests.get(API_URL)

parsed_data = json.loads(raw_data.text)

print(parsed_data)