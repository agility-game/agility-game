# server/src/agility_game/config/developmentConfig.py
from .baseConfig import BaseConfig


class DevelopmentConfig(BaseConfig):
    """
    Development environment specific configuration
    """

    SECRET_KEY = BaseConfig.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = BaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    DEBUG = True
    TESTING = True
    ENV = "Development"
