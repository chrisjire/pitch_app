import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:matthewwilliams@localhost/pitch_app'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'One Minute Pitch'
    SENDER_EMAIL = 'moringademo@gmail.com'
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:matthewwilliams@localhost/pitch_app'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}