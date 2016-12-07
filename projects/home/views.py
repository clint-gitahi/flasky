# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, session, flash, Blueprint
from functools import wraps
from projects import app, db  
from projects.model import BlogPost 
from flask_login import login_required


###############
####config#####
###############


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


###############
####routes#####
###############



# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template



@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

