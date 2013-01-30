# Global settings for photologue_demo project.

import os

# Note: the project dir is defined as the project python folder - not the outer
# container folder.  
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
    ('richard barran', 'richard@arbee-design.co.uk'),
)

MANAGERS = ADMINS

TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'public', 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3p0f5q)l$=gt++#z0inpfh%bm_ujl6(-yogbzw2)(xea48@70d'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photologue_demo.urls'

WSGI_APPLICATION = 'photologue_demo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'photologue',
    'photologue_demo',
    'south',
]

# A logging configuration that in dev writes log messages to the console.
# Note: check the path for the log file - might need adusting to fit your
# environment.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # Formatting of messages.
    'formatters': {
        # Don't need to show the time when logging to console.
        'console': {
            'format': '%(levelname)s %(module)s.%(funcName)s.%(lineno)d %(message)s'
        },
        'textlog': {
            'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s.%(lineno)d %(message)s'
        },
    },
    # Used by handlers to filter down the logs sent to it.
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    # The handlers decide what we should do with a logging message - do we email
    # it, ditch it, or write it to a file?
    'handlers': {
        # Writing to console. Use only in dev.
        'console': {
            'level': 'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'console'
        },
        # Writing to a log file.
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'textlog',
            'filename': '/var/log/django/photologue_demo.log',
        },
        # Mail error-level logs to the admins.
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # Send logs to /dev/null.
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
    },
    # Loggers decide what is logged.
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # In the requests, all errors get emailed to admins.
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # logging of SQL statements. Default is to ditch them (send them to
        # null). Note that this logger only works if DEBUG = True.
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

SOUTH_TESTS_MIGRATE = False
