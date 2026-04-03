import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost/info3180project1'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
