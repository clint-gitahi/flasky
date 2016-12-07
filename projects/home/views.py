# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, session, flash, Blueprint, request
from functools import wraps
from projects import app, db  
from projects.model import BlogPost 
from flask_login import login_required, current_user
from forms import MessageForm


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
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        print(new_message)
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template('index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

