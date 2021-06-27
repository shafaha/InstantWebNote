from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

class AppStarter:
    app  = Flask(__name__)
    app.config['SECRET_KEY'] = "SomeHexKeys"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)

    @classmethod
    def create_app(cls):
       return cls.app
    
    @classmethod
    def getDb(cls):
        return cls.db

    @classmethod
    def getBcrypt(cls):
        return cls.bcrypt

    @classmethod
    def getLoginManager(cls):
        return cls.login_manager


from .views import views
from .auth import auth
AppStarter.create_app().register_blueprint(views, url_prefix = '/')
AppStarter.create_app().register_blueprint(auth, url_prefix = '/')





