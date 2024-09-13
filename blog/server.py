from flask import Flask, render_template, Request
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    gender_request = requests.get(f"https://api.genderize.io?name={name.lower()}")
    gender = gender_request.json()['gender']
    age_request = requests.get(f"https://api.agify.io?name={name.lower()}")
    age = age_request.json()['age']
    return render_template('guess.html', name=name.title(), sex=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)


