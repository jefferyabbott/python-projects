from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        return f"Name: {request.form['name']}, Password: {request.form['password']}"
    else:
        return "Invalid data"

if __name__ == "__main__":
    app.run(debug=True)
