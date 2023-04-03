from twilio.rest import Client
import requests

account_sid = 'ACc4571e376dbaa8f0bec5b49be097280a'
auth_token = '667c423de63177af70baf22eba7a9ab4'
api_key = 'd78e49069b5aa160258b447776f9ac60'
endpoint = 'https://api.openweathermap.org/data/2.5/weather'


my_lat = -34.93168608132799
my_long = 138.60242422740995

weather_params = {
    'lat': my_lat,
    'lon': my_long,
    'appid': api_key
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
main_condition = weather_data['weather'][0]['main']
description = weather_data['weather'][0]['description']

if main_condition == 'rain':
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f'It\'s {description} right now',
        from_='+19896747379',
        to='+61459886112'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f'It\'s currently {description} outside! No need to bring umbrella',
        from_='+19896747379',
        to='+61459886112'
    )
