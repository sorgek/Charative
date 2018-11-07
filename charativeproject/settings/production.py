from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

print("using production settings")

ALLOWED_HOSTS = [
    'charative.herokuapp.com',
]
# Application definition

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

