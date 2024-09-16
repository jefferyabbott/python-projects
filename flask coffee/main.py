from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label = 'Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe location (Google Maps link)', validators=[URL()])
    opening_time = StringField(label='Opening time', validators=[DataRequired()])
    closing_time = StringField(label='Closing time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee rating', choices=[(0, '✘'), (1, '☕'), (2, '☕☕'), (3, '☕☕☕'), (4, '☕☕☕☕'), (5, '☕☕☕☕☕')])
    wifi_rating = SelectField(label='Wifi rating', choices=[(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    power_rating = SelectField(label='Power rating', choices=[(0, '✘'), (1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


def create_rating(emoji, qty):
    if int(qty) == 0:
        return '✘'
    rating = ''
    for _ in range(int(qty)):
        rating = rating + emoji
    return rating

def add_data_to_csv(data):
    file = open('cafe-data.csv', 'a')
    file.write('\n')
    file.write(data)
    file.close()

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location = form.location.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        coffee_rating = create_rating('☕', form.coffee_rating.data)
        wifi_rating = create_rating('💪', form.wifi_rating.data)
        power_rating = create_rating('🔌', form.wifi_rating.data)
        new_cafe_data = f"{cafe_name},{location},{opening_time},{closing_time},{coffee_rating},{wifi_rating},{power_rating}"
        add_data_to_csv(new_cafe_data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
