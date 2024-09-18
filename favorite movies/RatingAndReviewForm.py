from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RatingAndReviewForm(FlaskForm):
    rating = StringField(label="Your rating (out of 10)")
    review = StringField(label="Your review")
    submit = SubmitField(label="update")
