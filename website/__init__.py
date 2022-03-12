from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy() # db will be a type of database (SQLAlchemy)
DB_NAME = "database.db" # Name of database


def create_app():
    app = Flask(__name__) # Flask application
    app.config['SECRET_KEY'] = "secretkey"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # Application's database initialisation

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Like

    create_database(app) # Create database 

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    # Load all users were created 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME): # If database doesn't exist create it 
        db.create_all(app=app)
        print("Created database!")