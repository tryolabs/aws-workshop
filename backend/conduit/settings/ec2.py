import boto3
import json

from conduit.settings.defaults import *


client = boto3.client('ssm')
PARAMETERS_PATH = '/prod/api/'


def get_parameter(name, with_decryption=False, default=None):
    response = client.get_parameter(PARAMETERS_PATH + name, with_decryption)

    parameter = response.get('Parameter')
    if parameter:
        return parameter.get('Value')
    else:
        return default


DEBUG = get_parameter('DEBUG', default='False') == 'True'

ALLOWED_HOSTS = json.loads(get_parameter(
    'ALLOWED_HOSTS',
    default='["localhost", "127.0.0.1"]'
))


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


CORS_ORIGIN_WHITELIST = tuple(json.loads(get_parameter(
    'CORS_ORIGIN_WHITELIST',
    default='[]'
)))
