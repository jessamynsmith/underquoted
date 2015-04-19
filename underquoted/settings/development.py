from underquoted.settings.common import *

SECRET_KEY = 'oe3-zo6yeb34h*ktvana^ejbb(^du)613z+tl8@)psqkr+k7sd'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'underquoted',
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
SSLIFY_DISABLE = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
