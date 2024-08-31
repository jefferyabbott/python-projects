import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

query = input("Tell me which exercises you did: ")

url="https://trackapi.nutritionix.com"
endpoint="/v2/natural/exercise"

headers = {
    "x-app-id": os.getenv('NUTRITIONIX_APP_ID'),
    "x-app-key": os.getenv('NUTRITIONIX_API_KEY'),
}

params = {
    "query": query,
    "weight_kg": os.getenv('WEIGHT_KG'),
    "height_cm": os.getenv('HEIGHT_CM'),
    "age": os.getenv('AGE'),
}

exercise_response = requests.post(url=url+endpoint, headers=headers, json=params)
exercise_response.raise_for_status()
exercise = exercise_response.json()

sheety_url="https://api.sheety.co/"
sheety_endpoint="/myWorkouts/workouts"
sheety_url=f"{sheety_url}{os.getenv('SHEETY_ID')}{sheety_endpoint}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise["exercises"]:
    workouts = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

insert_exercise = requests.post(url=sheety_url, headers=sheety_headers, json=workouts)
insert_exercise.raise_for_status()
if insert_exercise.status_code == 200:
    print('Data inserted into Google sheet')
else:
    print("Data import failed.")
