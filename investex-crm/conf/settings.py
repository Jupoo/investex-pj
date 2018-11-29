"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

########## CORE
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '94j(o9ewgxv_tm5on^+am7%v*#(c_#j+hvy!af%gmgtuen)8^m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'conf.wsgi.application'

ROOT_URLCONF = 'conf.urls'

AUTH_USER_MODEL = 'core.Account'

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
########## END CORE


########## APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'ordered_model',
    'django_tables2',
]

INSTALLED_APPS += [
    'apps.core',
    'apps.clients',
    'apps.events',
    'apps.tracking',
]
########## END APPLICATIONS


########## MIDDLEWARES
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
########## END MIDDLEWARES


########## TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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
########## END TEMPLATES


########## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
########## END DATABASE


########## PASSWORD VALIDATION
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
########## END PASSWORD VALIDATION


########## LANGUAGES
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END LANGUAGES


########## STATIC
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/build'),
)
########## END STATIC


########## PROFILE SERVICE
PROFILE_SERVICE_URL = os.getenv('PROFILE_SERVICE_URL', 'http://auth:8000')

# oauth
OAUTH = {
    'OAUTH_HEADER_PREFIX': 'Bearer',
    'CLIENT_ID': os.getenv('CLIENT_ID', ''),
    'CLIENT_SECRET': os.getenv('CLIENT_SECRET', ''),
    'GRANT_TYPE': 'password',
    'AUTHORIZATION_URL': f'{PROFILE_SERVICE_URL}/o/authorize/',
    'RESOURCE_SERVER_URL': f'{PROFILE_SERVICE_URL}/o/introspect/',
    'TOKEN_URL': f'{PROFILE_SERVICE_URL}/o/token/',

    'USER_INFO_URL': f'{PROFILE_SERVICE_URL}/api/v1/get-user/',
    'USERNAME_FIELD': 'email',
    'KEY_FIELD': 'id',
    'USER_FIELD_MAPPINGS': {'email': 'email'},
    'USER_CREATION_FUNCTION': 'apps.accounts.utils.auto_create_user',
}
########## END PROFILE SERVICE


########## CELERY
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:6379/'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# periodic tasks crontabs
UPDATE_PER_DAY_STATS = {
    'minute': '*/1'
}
########## END CELERY


########## INTEGRATIONS
DASHBOARD_URL = os.getenv('DASHBOARD_URL', 'http://127.0.0.1:8000')
PARTNER_URL = os.getenv('PARTNER_URL', 'http://127.0.0.1:8001')
########## END INTEGRATIONS