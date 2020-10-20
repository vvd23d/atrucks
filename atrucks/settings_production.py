from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os

ALLOWED_HOSTS = ['localhost', '192.168.111.43']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'atrucks',
        'USER': 'atrucks',
        'PASSWORD': 'atrucks',
        'HOST': 'db',
        'PORT': '5432',
    }

}

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
