from os import path

basedir = path.abspath(path.dirname(__file__))

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_APP = 'app.py'
    SECRET_KEY = "mysecretkey"
    HOST='0.0.0.0' # Set the host to '0.0.0.0' to don't have the localhost
    PORT=7007 # Set the port to 7007


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False