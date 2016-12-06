from app import db
from model import User

# insert data
db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("admins", "ad@min.com", "admins"))

# commit the changes
db.session.commit()