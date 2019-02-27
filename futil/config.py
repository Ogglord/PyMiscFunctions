import tempfile

class Config:
    APP_NAME = 'OKQ8_DK'
    SECRET_KEY = 'secret-key-of-myapp'
    
    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880 # 5MB

    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = None
    REDIS_PWD = None

    TMP_FOLDER = tempfile.gettempdir() #override to change default tmp folder  

    FTP_HOST = None
    FTP_DIR = '/'
    FTP_PORT = 21
    FTP_FILTER = '*.xlsx'
    FTP_USERNAME = None
    FTP_PWD = None

 
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestConfig(Config):
    FTP_HOST = 'ftp.sunet.se'
    FTP_DIR = '/pub/putty/putty-latest/'
    FTP_PORT = 21
    FTP_FILTER = '*.txt'
    FTP_USERNAME = None
    FTP_PWD = None

    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    