#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
import os



# config 
app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from projects.users.views import users_blueprint
from projects.home.views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

from model import User 

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()