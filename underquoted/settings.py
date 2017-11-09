import dateutil.parser
import dj_database_url
import os

from email.utils import formataddr


HOME_DIR = os.path.expanduser("~")
BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'oe3-zo6yeb34h*ktvana^ejbb(^du)613z+tl8@)psqkr+k7sd')

# Use env setting if available, otherwise make debug false
DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', '0')))
TEMPLATE_DEBUG = DEBUG

SSLIFY_DISABLE = not bool(int(os.environ.get('DJANGO_ENABLE_SSL', '0')))
ALLOWED_HOSTS = ['underquoted.herokuapp.com', 'localhost', '127.0.0.1']

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

ADMINS = (
    (os.environ.get('ADMIN_NAME', 'admin'), os.environ.get('ADMIN_EMAIL', 'example@example.com')),
)

SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Toronto'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Static asset configuration
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'underquoted', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'underquoted.urls'

CORS_ORIGIN_ALLOW_ALL = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'underquoted.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'underquoted', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.request",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "settings_context_processor.context_processors.settings",
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'corsheaders',
    'settings_context_processor',
    'djorm_pgfulltext',
    'rest_framework',
    'tastypie',
    'api',
    'quotations',
]

PAGE_SIZE = 5

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

MAX_PER_PAGE = 5

DEFAULT_FROM_EMAIL = formataddr(ADMINS[0])
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True

if not EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(HOME_DIR, 'underquoted', 'emails')

DEPLOY_DATE = dateutil.parser.parse(os.environ.get('DEPLOY_DATE', ''))
VERSION = '0.1'

TEMPLATE_VISIBLE_SETTINGS = ['DEPLOY_DATE', 'VERSION']

TEST_RUNNER = 'django.test.runner.DiscoverRunner'