from .base import *  # noqa

DEBUG = True

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
}

SECRET_KEY="BIGBLUEBALLS1234567890!!!!THERESnowayIknowthislol7757747747374234"