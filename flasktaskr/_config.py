import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'I\x88\xa0.\x01#\xd5+\x12w\xa0\xa8[46.yh\xcfSH\xff4\x1e'

DATABASE_PATH = os.path.join(basedir,DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ DATABASE_PATH

