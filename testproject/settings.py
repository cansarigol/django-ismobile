
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'SECRET_KEY'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'ismobile'
]

MIDDLEWARE = [
    'ismobile.middleware.MobileControlMiddleware'
]

ROOT_URLCONF = 'testproject.urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
