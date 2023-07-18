from pathlib import Path
from dotenv import load_dotenv
import os
import logging
from django import utils

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gv4t*@8w6=i(!kt*_#u76l&fhcwur@wy*1(v@^%hx_zfgk1j1e'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
SITE_URL = 'http://127.0.0.1:8000'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'accounts.apps.AccountsConfig',
    'sign',
    'protect',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

SITE_ID = 1

LOGIN_URL = 'sign/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'info': {
            'format': '[%(asctime)s] %(levelname)s %(module)s: %(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'debug': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'warning': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s "%(pathname)s"',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
        'errors': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s "%(pathname)s" %(exc_info)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console-debug': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'debug',
            'filters': ['require_debug_true', ],
        },
        'console-warning': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'warning',
            'filters': ['require_debug_true'],
        },
        'console-error': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'errors',
            'filters': ['require_debug_true'],
        },
        'file-info': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'info',
            'filters': ['require_debug_false', ],
            'filename': '../logging/general.log',
        },
        'file-errors': {
            'class': 'logging.FileHandler',
            'level': ['ERROR'],
            'formatter': 'errors',
            'filename': '../logging/errors.log',
        },
        'mail-admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
        },
        'file-security': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'info',
            'filename': '../logging/security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console-info', 'console-warning', 'console-error', 'file-info', ],
        },
        'django.security': {
            'handlers': ['file-security', ],
        },
        'django.request': {
            'handlers': ['file-errors', 'mail-admins', ],
            'level': 'ERROR',
        },
        'django.server': {
            'handlers': ['file-errors', 'mail-admins', ],
            'level': 'ERROR',
        },
        'django.template': {
            'handlers': ['file-errors', ],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['file-errors', ],
            'level': 'ERROR',
        },
    },
}
