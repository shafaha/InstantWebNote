from note import AppStarter
from datetime import datetime
from flask_login import UserMixin



db = AppStarter.getDb()
login_manager = AppStarter.getLoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)
    notes = db.relationship("Notes", backref = "creator", lazy = True)

    def __init__(self, uname, eml, pwd):
        self.username = uname
        self.email = eml
        self.password = pwd

    def __repr__(self):
        return "Username: " + self.username + " email: " + self.email 

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, nullable =  False, default = datetime.utcnow)
    description = db.Column(db.String(500), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, dex, d):
        self.title = title
        self.description = dex
        self.user_id = d


    

