class Config:
    APP_NAME = 'OKQ8_DK'
    SECRET_KEY = 'secret-key-of-myapp'
    
    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880 # 5MB

    REDIS_PORT = 6379
    REDIS_HOST = "localhost"
    REDIS_DB = None
    REDIS_PWD = None

    TMP_FOLDER = None # Use this to override the default OS tmp folder
    

class DevelopmentConfig(Config):
    DEBUG = True
    
class TestConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    