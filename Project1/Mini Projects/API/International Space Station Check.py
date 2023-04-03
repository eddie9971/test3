import requests
from datetime import datetime


def can_see():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if my_lat - 5 <= latitude <= my_lat + 5 and my_long - 5 <= longitude <= my_long + 5:
        return True


my_lat = -34.93168608132799
my_long = 138.60242422740995


def is_night():
    parameters = {
        'lat': my_lat,
        'lng': my_long,
        'formatted': 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if can_see() and is_night():
    print('You can see the Internation Space Station')
else:
    print('You can not see it in the sky')

