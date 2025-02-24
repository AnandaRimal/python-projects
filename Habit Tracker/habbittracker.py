import os
import requests
from datetime import datetime

USERNAME = "anandarimal1"
TOKEN = os.getenv("token")
GRAPH_ID = "coding-graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print("User Creation Response:", response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("Graph Creation Response:", response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Pixel Creation Response:", response.text)
