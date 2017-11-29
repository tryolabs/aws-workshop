import boto3
import json

from botocore.exceptions import ClientError

from conduit.settings.defaults import *


client = boto3.client('ssm')
PARAMETERS_PATH = '/prod/api/'

def get_parameter(name, with_decryption=False, default=None):
    try:
        response = client.get_parameter(
            Name=PARAMETERS_PATH + name,
            WithDecryption=with_decryption
        )

        parameter = response.get('Parameter')
        return parameter.get('Value')
    except ClientError as e:
        if e.response['Error']['Code'] == 'ParameterNotFound':
            return default
        else:
            raise e


DEBUG = get_parameter('DEBUG', default='False') == 'True'


STATIC_ROOT = '/var/www/conduit/static/'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_parameter('DATABASE_NAME'),
        'USER': get_parameter('DATABASE_USER'),
        'PASSWORD': get_parameter('DATABASE_PASSWORD', True),
        'HOST': get_parameter('DATABASE_HOST'),
        'PORT': get_parameter('DATABASE_PORT', default='5432'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'django.file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/django.log',
        },
        'django.security.file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/django.security.log',
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

CORS_ORIGIN_WHITELIST = tuple(json.loads(get_parameter(
    'CORS_ORIGIN_WHITELIST',
    default='[]'
)))

CORS_ORIGIN_ALLOW_ALL = True
