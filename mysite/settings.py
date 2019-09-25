"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
from .secret import access_key_id, secret_access_key, bucket_name, django_secret_key
SECRET_KEY = django_secret_key



import os
import django_heroku
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tranquil-savannah-79167.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mod.apps.ModConfig',
    'accounts.apps.AccountsConfig',
    'taggit',
    'django_filters',
    'taggit_templatetags2',
    'secretballot',
    'likes',
    'progressbarupload',
    'django_cleanup.apps.CleanupConfig',
    'easy_thumbnails',
    'pages.apps.PagesConfig',
    'embed_video',
    'taggit_selectize',
    'verified_email_field',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'secretballot.middleware.SecretBallotIpUseragentMiddleware',
    'likes.middleware.SecretBallotIpUseragentMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_URL = '/static/'

STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/files/'

LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
DEFAULT_FROM_EMAIL = "yaes@example.com"

AUTH_USER_MODEL = 'accounts.User'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

TAGGIT_CASE_INSENSITIVE = True

PINAX_RATINGS_CATEGORY_CHOICES = {
    "mod.Mod": {
        "rating": "Rating of the mod."
    }
}

FILE_UPLOAD_HANDLERS = (
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

MAX_UPLOAD_SIZE = 859832320

MAX_AVATAR_UPLOAD_SIZE = 10485760

MAX_BACKGROUND_UPLOAD_SIZE = 20971520

THUMBNAIL_ALIASES = {
    'mod': {
        'avatar': {'size': {200, 200}, 'crop': 'smart', 'autocrop': True}
    }
}


TAGGIT_TAGS_FROM_STRING = 'taggit_selectize.utils.parse_tags'
TAGGIT_STRING_FROM_TAGS = 'taggit_selectize.utils.join_tags'

TAGGIT_SELECTIZE = {
    'MINIMUM_QUERY_LENGTH': 2,
    'RECOMMENDATION_LIMIT': 10,
    'CSS_FILENAMES': ("taggit_selectize/css/selectize.django.css",),
    'JS_FILENAMES': ("taggit_selectize/js/selectize.js",),
    'DIACRITICS': True,
    'CREATE': True,
    'PERSIST': True,
    'OPEN_ON_FOCUS': True,
    'HIDE_SELECTED': True,
    'CLOSE_AFTER_SELECT': False,
    'LOAD_THROTTLE': 300,
    'PRELOAD': False,
    'ADD_PRECEDENCE': False,
    'SELECT_ON_TAB': False,
    'REMOVE_BUTTON': False,
    'RESTORE_ON_BACKSPACE': False,
    'DRAG_DROP': False,
    'DELIMITER': ','
}

EMAIL_CONFIRMATION_PERIOD_DAYS = 7
SIMPLE_EMAIL_CONFIRMATION_PERIOD = timedelta(days=EMAIL_CONFIRMATION_PERIOD_DAYS)

SECURE_SSL_REDIRECT = True  #developemnt change to False

#AWS_ACCESS_KEY_ID = access_key_id
#AWS_SECRET_ACCESS_KEY = secret_access_key
#AWS_STORAGE_BUCKET_NAME = bucket_name
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400',
#}
#AWS_LOCATION = 'static'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD=True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

django_heroku.settings(locals())

#LOGGING_CONFIG = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "")
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN", "")
MEDIA_ROOT = os.environ.get("MEDIA_URL", "")
STATIC_URL = os.environ.get("STATIC_URL", "")

AWS_DEFAULT_ACL = None