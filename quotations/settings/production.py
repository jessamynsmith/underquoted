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

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

ALLOWED_HOSTS = ['underquoted.herokuapp.com']

INSTALLED_APPS.extend([
    'gunicorn',
])
