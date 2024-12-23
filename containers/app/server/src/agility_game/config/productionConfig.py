# server/src/agility_game/config/productionConfig.py
from .baseConfig import BaseConfig


class ProductionConfig(BaseConfig):
    """
    Production specific config
    """

    SECRET_KEY = BaseConfig.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = BaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    DEBUG = False
    ENV = "Production"
