class BaseConfig(object):
    FLASK_DEBUG = True
    SECRET_KEY = 'flask-session-insecure-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://megatrack:megatrack@localhost:3306/megatracktest'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_FILE_PATH = '../data/' # relative to views module
    LOG_FILE_PATH = 'log/megatrack.log'