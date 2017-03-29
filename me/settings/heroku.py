from .base import *
from decouple import ConfigIni
import dj_database_url

config = ConfigIni(PROJECT_DIR.child('infra_confs')+'/settings.ini')

DEBUG = True
BASE_DIR = PROJECT_DIR
PROJECT_ROOT = Path(__file__)

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

INSTALLED_APPS += (
    'gunicorn',
)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

DATABASES['default'] = dj_database_url.config(conn_max_age=500)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARD_PROTO', 'https')

ALLOWED_HOSTS = [
    '*',
    'meusersapi.herokuapp.com'
]
