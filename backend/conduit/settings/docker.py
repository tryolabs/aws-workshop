import json
import os

from conduit.settings.defaults import *


DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'


STATIC_ROOT = '/data/static/'


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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'django.file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/data/django.log',
        },
        'django.security.file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/data/django.security.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django.file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['django.security.file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': [],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


CORS_ORIGIN_WHITELIST = tuple(json.loads(os.environ.get(
    'DJANGO_CORS_ORIGIN_WHITELIST',
    '[]'
)))
