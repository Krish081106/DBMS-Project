from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    genre = db.Column(db.String(120), nullable=True)
    image = db.Column(db.String(255), nullable=True)

class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    seats = db.Column(db.String(100), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    movie = db.relationship('Movie', backref='bookings')
