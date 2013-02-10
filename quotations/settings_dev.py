from settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'quotations',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'TEST_NAME': 'test_quotations',
    }
}

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = '/tmp'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
