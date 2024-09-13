from flask import Flask, render_template, Request
import requests


app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    gender_request = requests.get(f"https://api.genderize.io?name={name.lower()}")
    gender = gender_request.json()['gender']
    age_request = requests.get(f"https://api.agify.io?name={name.lower()}")
    age = age_request.json()['age']
    return render_template('guess.html', name=name.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)


