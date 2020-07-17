from decouple import config


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
