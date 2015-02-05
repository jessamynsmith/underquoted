from quotations.settings.common import *

import os

SECRET_KEY = 'oe3-zo6yeb34h*ktvana^ejbb(^du)613z+tl8@)psqkr+k7sd'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quotations',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/tmp/static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = '/tmp/media'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS.extend([
    'django_nose',
])

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DJANGO_ARGS = [
    '--verbosity=0',
]

NOSE_ARGS = [
    '--exclude=settings',
    '--verbosity=0',
    '--cover-branches',
    '--cover-package=quotations',
    '--cover-inclusive',  # Cover all files
    '--cover-html',
    '--cover-html-dir=%s/quotations_coverage' % os.environ.get('HOME'),
]
