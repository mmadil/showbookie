# Django absolute path for settings.py

import os
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here('..')
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)


# Django settings for showbookie project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG
PRODUCTION = True

ADMINS = (
    ('Mohammad Adil', 'mmadil_14@yahoo.com'),
)

LOGIN_URL = "/accounts/login/"

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*',]

COMMENTS_HIDE_REMOVED = True
REGISTRATION_OPEN = True

# Django Haystack Settings

HAYSTACK_SEARCH_RESULT_PER_PAGE = 20

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        },
}


# Django registration settings
LOGIN_REDIRECT_URL = '/'
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u:'/profile/%s' % u.username,
}

RATINGS_VOTES_PER_IP = 20

ANONYMOUS_USER_ID = -1

TIME_ZONE = 'Asia/Kolkata'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18 = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = root('..','uploads')
MEDIA_URL = '/uploads/'

STATIC_ROOT = root('..','static')

STATICFILES_DIRS = (
        root('..','assets'),
)

TEMPLATE_DIRS = (
        root('..','templates'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'w$(2*sg$+qwdq-j8cw2o4skxc*yhniw@-yhakyhb(8#o$cd9*i'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'showbookie.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'showbookie.wsgi.application'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.admin',
)

COMMENTS_APP = 'reviews'

LOCAL_APPS = (
    'reviews',
    'movies',
    'profiles',
)

THIRD_PARTY_APPS = (
    'haystack',
    'south',
    'braces',
    'guardian',
    'registration',
    'djangoratings',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS 

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from local_settings import *
except ImportError:
    pass

if PRODUCTION:
    STATIC_URL = 'https://googledrive.com/host/0B-gIhJMz12BtVVBPRHBhdjFPZkk/'
else:
    STATIC_URL = '/static/'

