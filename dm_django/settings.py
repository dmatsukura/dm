"""
Django settings for dm_django project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import environ
from pathlib import Path


#Initialize environment variables
env = environ.Env()
environ.Env.read_env()

PRODUCTION = (env("PRODUCTION") == '1') #1 is dev and 0 is production

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-fsw(@h2^x5=rri^jj!59&w#^qsdj#=t8&)5%4-@x$mx$_aewqq'
#SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#DEBUG = bool(os.environ.get("DEBUG", default=1))

if PRODUCTION:
    DEBUG = False
else:
    DEBUG = True

#ALLOWED_HOSTS = []

#if PRODUCTION:
#    ALLOWED_HOSTS = [os.uname()[1], "192.168.11.211"]
#else:
#ALLOWED_HOSTS = ["192.168.11.211", "localhost", "*", "dm_django.localhost"]

if PRODUCTION:
    ALLOWED_HOSTS = ["matsukura.dev", "192.168.11.211"]
else:
    ALLOWED_HOSTS = [os.uname()[1],"192.168.11.211", "localhost", "*", "dm_django.localhost"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', #Downloaded App from GitHub(git clone https://github.com/django-extensions/django-extensions.gits)
    'django_celery_beat',
    'django_celery_results',
    'dm_django',
    'private_storage',
    'django_rename_app',
    'dm_portfolio', 
    'ckeditor', 
    'rest_framework',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'accounts',
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

ROOT_URLCONF = 'dm_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dm_portfolio.context_processors.project_context'
            ],
            'debug': DEBUG,
        }
    },
]

WSGI_APPLICATION = 'dm_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #},
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT")
    }
    ,
    'nc': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("NC_DATABASE_NAME"),
        'USER': env("NC_DATABASE_USER"),
        'PASSWORD': env("NC_DATABASE_PASSWORD"),
        'HOST': env("NC_DATABASE_HOST"),
        'PORT': env("NC_DATABASE_PORT")
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

if PRODUCTION:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
else:
    # Don't send to production emails receivers in development
    EMAIL_BACKEND = "django.core.email.backends.dummy.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
#
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_URL = '/static/'


if PRODUCTION:
    STATIC_ROOT = "/home/administrator/dm_nc_sync/dm_django_static/production_static/static/"

else:
    STATIC_ROOT = "/home/administrator/dm_nc_sync/dm_django_static/dev_static/static/"
STATIC_URL = "/static/static/"


MEDIA_ROOT = "/home/dm_nc_sync/dm_django_media/img/"
MEDIA_URL = "img/img/"

#PRIVATE_STORAGE_ROOT = MEDIA_ROOT
#PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_authenticated'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Logging
LOGGING_DIR = '/home/administrator/dm_nc_sync/dm_django_log/log'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'mail_admins', 'console'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['default'],
            'level': 'INFO',
            "propagate": True,
        },
        'django.db.backends': {
            'level': 'WARNING',
        },
        'asyncio': {  # Stop obnoxious EpollSelector log messages
            'level': 'WARNING',
        }
    }
}
