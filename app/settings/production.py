import os
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'prod-back-app.herokuapp.com',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3t0raofepdll0',
        'USER': 'vlgggelwlnrzlz',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'ec2-54-228-174-49.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ORIGIN_WHITELIST = ['https://www.wattplanner.ovh']
