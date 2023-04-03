import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': 'sdg34rgqehngaf',
    'username': 'eddie123',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

username = user_params['username']
token = user_params['token']

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_confix = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': token
}

# response = requests.post(url=graph_endpoint, json=graph_confix,headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'

today = datetime.now().strftime('%Y%m%d')

pixel_data = {
    'date': today,
    'quantity': '10.12',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

print(today)