from flask import Flask, render_template, Response, request
from post import Post
import requests
import re
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

blog_url = "https://api.npoint.io/7f327db812dc5ebc6f34"
post_data = requests.get(blog_url).json()
posts = []
for post in post_data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"])
    posts.append(post_obj)


def is_valid_email(email: str) -> bool:
    # Regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False


def send_email(form_data):
    my_email = os.getenv('MY_EMAIL')
    email_password = os.getenv('MY_EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    target_email = os.getenv('TARGET_EMAIL')

    with smtplib.SMTP(smtp_server, int(smtp_port)) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:{form_data['subject']}\n\nFrom: {form_data['name']} / {form_data['email']} ... {form_data['message']}"
        )

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html', msg_sent=False)
    elif request.method == "POST" and is_valid_email(request.form['data']):
        form_data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "message": request.form['message']
        }
        send_email(form_data)
        return render_template('contact.html', msg_sent=True)
    else:
        return "<h1>Invalid data</h1>"

@app.route('/post/<search_id>')
def post(search_id):
    found_post = None
    for post_item in posts:
        if post_item.post_id == int(search_id):
            found_post = post_item
    if found_post is not None:
        return render_template('post.html', post=found_post)
    else:
        return Response(status = 404)

if __name__ == "__main__":
    app.run(debug=True)
