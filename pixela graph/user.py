import os
from dotenv import load_dotenv
load_dotenv()

user_params = {
    "token": os.getenv('TOKEN'),
    "username": os.getenv('USERNAME'),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}