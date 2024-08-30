import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# post a pixel
pixela_pixel_url = f"https://pixe.la/v1/users/{os.getenv('USERNAME')}/graphs/{os.getenv('GRAPH_ID')}"

headers = {
    "X-USER-TOKEN": os.getenv('TOKEN'),
}

today = datetime.now().strftime('%Y%m%d')

pixel_body = {
    "date": today,
    "quantity": "2.01",
}

response = requests.post(url=pixela_pixel_url, json=pixel_body, headers=headers)
print(response.text)
