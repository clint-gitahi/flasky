# import the Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
import os


# config 
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from projects.users.views import users_blueprint
from projects.home.views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)