"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = 'myappsecret'       # environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = 'myappsecret_session_cookie'    #environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static/'
    STATIC_IMG_FOLDER = 'static/images/'
    TEMPLATES_FOLDER = 'templates'




class ProdConfig(Config):
    # Define Production specifed settings

    ENV = 'production'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')
    INSECURE_TRANSPORT = '0'
    DOMAIN_ROOT = 'http://103.237.146.126/'


class DevConfig(Config):
    # Define Development specifed settings
    
    ENV = 'development'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    INSECURE_TRANSPORT = '1'
    DOMAIN_ROOT = 'http://localhost:5000/'