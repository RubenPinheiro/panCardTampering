import os
from os import environ


class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'montadaProjects'

    UPLOADS = '/home/username/app/app/static/uploads'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    INITIAL_FILE_UPLOADS = 'app/static/uploads'
    EXISTING_FILE = 'app/static/original'
    GENERATED_FILE = 'app/static/generated'

class DebugConfig(Config):
    DEBUG = False