from flask import Flask, render_template, Response
from post import Post
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/7f327db812dc5ebc6f34"
post_data = requests.get(blog_url).json()
posts = []
for post in post_data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"])
    posts.append(post_obj)

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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
