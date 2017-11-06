import json
import os

from conduit.settings.defaults import *


DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = json.loads(os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    '["localhost", "127.0.0.1"]'
))


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


CORS_ORIGIN_WHITELIST = tuple(json.loads(os.environ.get(
    'DJANGO_CORS_ORIGIN_WHITELIST',
    '[]'
)))
