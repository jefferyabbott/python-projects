import requests
import os
from dotenv import load_dotenv
load_dotenv()

date_to_delete = "20240830"

# delete a pixel
pixela_pixel_url = f"https://pixe.la/v1/users/{os.getenv('USERNAME')}/graphs/{os.getenv('GRAPH_ID')}/{date_to_delete}"

headers = {
    "X-USER-TOKEN": os.getenv('TOKEN'),
}

response = requests.delete(url=pixela_pixel_url, headers=headers)
print(response.text)
