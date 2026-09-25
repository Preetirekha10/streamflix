from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///streamflix.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(500))


@app.route("/")
def home():

    search = request.args.get("search", "")

    if search:
        movies = Movie.query.filter(
            Movie.title.ilike(f"%{search}%")
        ).all()
    else:
        movies = Movie.query.all()

    return render_template(
        "index.html",
        movies=movies,
        search=search
    )

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):

    movie = Movie.query.get_or_404(movie_id)

    return render_template(
        "movie.html",
        movie=movie
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

        if Movie.query.count() == 0:

            movies = [
                Movie(
                    title="Inception",
                    genre="Sci-Fi",
                    year=2010,
                    rating=8.8,
                    description="A skilled thief enters people's dreams.",
                    poster_url="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"
                ),

                Movie(
                    title="Interstellar",
                    genre="Sci-Fi",
                    year=2014,
                    rating=8.7,
                    description="A team travels through space searching for a new home.",
                    poster_url="https://images.unsplash.com/photo-1446776877081-d282a0f896e2"
                ),

                Movie(
                    title="The Dark Knight",
                    genre="Action",
                    year=2008,
                    rating=9.0,
                    description="Batman faces a dangerous criminal in Gotham City.",
                    poster_url="https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c"
                ),

                Movie(
                    title="Joker",
                    genre="Drama",
                    year=2019,
                    rating=8.4,
                    description="A troubled man begins a transformation into a criminal figure.",
                    poster_url="https://images.unsplash.com/photo-1485846234645-a62644f84728"
                )
            ]

            db.session.add_all(movies)
            db.session.commit()

    app.run(debug=True)