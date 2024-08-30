import requests
from user import user_params

# create user
pixela_user_url = "https://pixe.la/v1/users"
response = requests.post(url=pixela_user_url, json=user_params)
print(response.text)