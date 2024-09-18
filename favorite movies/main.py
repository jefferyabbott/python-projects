from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from RatingAndReviewForm import RatingAndReviewForm
from AddMovieForm import AddMovieForm
import requests
import os
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    movies = result.scalars().all()
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=["GET", "POST"])
def edit_review_and_rating():
    form = RatingAndReviewForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    with app.app_context():
        movie_id = request.args.get('id')
        movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        user_search = form['title'].data
        url = f"https://api.themoviedb.org/3/search/movie?query={user_search}&include_adult=false&language=en-US&page=1"
        headers = {"accept": "application/json",
                   "Authorization": f"Bearer {os.getenv('TMDB_TOKEN')}"}
        response = requests.get(url, headers=headers)
        return render_template('select.html', results=response.json()['results'])
    return render_template('add.html', form=form)

@app.route("/select")
def select_movie():
    title = request.args.get('title')
    year = int(request.args.get('year'))
    description = request.args.get('description')
    img_url = request.args.get('img_url')
    new_movie = Movie(
        title = title,
        year = year,
        description = description,
        rating = 0,
        ranking = 0,
        review = "",
        img_url = f"https://image.tmdb.org/t/p/w500/{img_url}"
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_review_and_rating', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
