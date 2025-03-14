from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cake-details')
def cake_details():
    return render_template('cake-details.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')