import os

from thepursuit.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','13.126.226.206','thepursuit.tedxpesitbsc.com','tiusrupeht.ingeniushack.com']

#ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'thepursuit',                 # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'tedx',
        'PASSWORD': 'tedx',
        'HOST': 'localhost',                 # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
