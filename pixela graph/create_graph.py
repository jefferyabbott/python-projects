import requests
import os
from dotenv import load_dotenv
load_dotenv()

# create graph
pixela_graph_url = f"https://pixe.la/v1/users/{os.getenv('USERNAME')}/graphs"

headers = {
    "X-USER-TOKEN": os.getenv('TOKEN'),
}

graph_config = {
    "id": os.getenv('GRAPH_ID'),
    "name": "Swimming Graph",
    "unit": "Miles",
    "type": "float",
    "color": "sora",
}

response = requests.post(url=pixela_graph_url, json=graph_config, headers=headers)
print(response.text)