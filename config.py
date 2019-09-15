import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:matthewwilliams@localhost/pitch_app'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:matthewwilliams@localhost/pitch_app'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}