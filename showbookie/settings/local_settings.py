DEBUG = True
TEMPLATE_DEBUG = DEBUG
PRODUCTION = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
    }
}

