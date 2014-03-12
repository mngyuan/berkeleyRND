from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

SECRET_KEY = 'SO_RANDOM'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'projectdb.db')
SQLALCHEMY_ECHO = True
