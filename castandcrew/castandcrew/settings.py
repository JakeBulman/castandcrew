"""
Django settings for castandcrew project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

import json
import boto3

load_dotenv(find_dotenv())

#Load all env variables from secrets manager
secret_name = os.getenv('SECRET_LOCATION')
region_name = 'eu-north-1'
session = boto3.session.Session(aws_access_key_id=os.getenv('AWS_SERVER_PUBLIC_KEY'),aws_secret_access_key=os.getenv('AWS_SERVER_SECRET_KEY'))
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)
secrets = client.get_secret_value(SecretId=secret_name)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = json.loads(secrets['SecretString'])['SECRET_KEY'],

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','13.51.169.173','thecastandcrew.co.uk','www.thecastandcrew.co.uk','lokey.co.uk','www.lokey.co.uk']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #other apps
    'compressor',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'castandcrew.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),BASE_DIR / "castandcrew/templates", BASE_DIR / "/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'castandcrew.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'castandcrew',
#         'USER': os.getenv('POSTGRES_USER'), castandcrew
#         'PASSWORD': os.getenv('DB_PASSWORD'), jman
#         'HOST': 'localhost',
#         'PORT': '5433',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': json.loads(secrets['SecretString'])['DB_NAME'],
        'USER': json.loads(secrets['SecretString'])['POSTGRES_USER'],
        'PASSWORD': json.loads(secrets['SecretString'])['DB_PASSWORD'],
        'HOST': json.loads(secrets['SecretString'])['DB_HOST'],
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (    
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

USING_S3 = json.loads(secrets['SecretString'])['USING_S3'] == 'True'

if USING_S3:
    print('S3 is on')
    AWS_ACCESS_KEY_ID = json.loads(secrets['SecretString'])['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = json.loads(secrets['SecretString'])['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = json.loads(secrets['SecretString'])['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_SIGNATURE_NAME = json.loads(secrets['SecretString'])['AWS_S3_SIGNATURE_NAME']
    AWS_S3_REGION_NAME = json.loads(secrets['SecretString'])['AWS_S3_REGION_NAME']
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_VERITY = True
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_ROOT = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
