from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# ---------- APP SETUP ----------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:KrishS%21%400558@localhost/movie_booking_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

# ---------- MODELS ----------
class Movie(db.Model):
    __tablename__ = "movies"   #  Must match foreign key reference
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    genre = db.Column(db.String(120), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    show_time = db.Column(db.String(50), nullable=False)
    screen = db.Column(db.String(50), nullable=False)


class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    seats = db.Column(db.String(100), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)  # ✅ Foreign key corrected
    movie_name = db.Column(db.String(120), nullable=False)

    # Relationship to Movie
    movie = db.relationship('Movie', backref='bookings')

# ---------- ROUTES ----------
@app.route('/')
def home():
    """Home page displaying all movies"""
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.route('/movie/<int:id>')
def movie_page(id):
    """Display selected movie & seat selection page"""
    movie = Movie.query.get_or_404(id)
    seats = [f"{row}{num}" for row in "ABC" for num in range(1, 7)]  # Example seat layout A1–C6
    return render_template('movie.html', movie=movie, seats=seats)


@app.route('/book', methods=['POST'])
def book_ticket():
    """Handle ticket booking form submission"""
    user_name = request.form['name']
    # user_email = request.form['email']
    movie_id = request.form['movie_id']
    selected_seats = request.form.getlist('seats')
    total_price = len(selected_seats) * 150  # ₹150 per seat

    movie = Movie.query.get(movie_id)

    booking = Booking(
        user_name=user_name,
        user_email="aaa@gmail.com",
        movie_id=movie.id,
        movie_name=movie.title,  #  Store movie name too
        seats=",".join(selected_seats),
        total_price=total_price
    )
    db.session.add(booking)
    db.session.commit()

    bookings = {"name": user_name, "movie_tit": movie.title, "seats": ",".join(selected_seats), "total_price": total_price, "timings": movie.show_time}

    flash('🎟 Booking successful! Confirmation sent to your email.', 'success')
    return render_template('booking_success.html', booking=bookings)


# ---------- INITIALIZE DATABASE ----------
with app.app_context():
    db.create_all()


# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)