# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

# create the sqlalchemy object
db = SQLAlchemy(app)

# import db schema
from model import *

# login required decorator 
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to loggin first')
            return redirect(url_for('login'))
    return wrap 

# use decorators to link the funciton to url 
@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    # render the welcome template.
    return render_template('welcome.html')

# handling the login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None 
    if request.method == 'POST':
        if (request.form['username'] != 'admin') or request.form['password'] != 'admin':
            error = "Invalid login. Please try again."
        else:
            session['logged_in'] = True
            flash('You are now logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You logged out.")
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()