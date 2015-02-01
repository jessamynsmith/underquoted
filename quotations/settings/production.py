from quotations.settings.common import *

import dj_database_url
import os

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

APP_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                         os.path.pardir))

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = "/%s/" % STATIC_S3_PATH

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME

ALLOWED_HOSTS = ['underquoted.herokuapp.com']

INSTALLED_APPS.extend([
    's3_folder_storage',
    'storages',
    'gunicorn',
])