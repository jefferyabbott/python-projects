import requests
import os
from dotenv import load_dotenv
load_dotenv()

date_to_update = "20240830"

# update a pixel
pixela_pixel_url = f"https://pixe.la/v1/users/{os.getenv('USERNAME')}/graphs/{os.getenv('GRAPH_ID')}/{date_to_update}"

headers = {
    "X-USER-TOKEN": os.getenv('TOKEN'),
}

pixel_body = {
    "quantity": "2.56",
}

response = requests.put(url=pixela_pixel_url, json=pixel_body, headers=headers)
print(response.text)
