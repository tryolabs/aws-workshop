import boto3
import json
import os

from botocore.exceptions import ClientError

from conduit.settings.defaults import *


client = boto3.client('ssm')
PARAMETERS_PATH = '/prod/api/'

EC2_HOSTNAME = os.environ['EC2_PUBLIC_HOSTNAME']
EC2_IP = os.environ['EC2_PUBLIC_IP']


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

ALLOWED_HOSTS = json.loads(get_parameter(
    'ALLOWED_HOSTS',
    default='["{}", "{}"]'.format(EC2_HOSTNAME, EC2_IP)
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
