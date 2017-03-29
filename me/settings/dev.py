import os
from .base import *
from decouple import ConfigIni
import dj_database_url

# ######### DEBUG CONFIGURATION
DEBUG = True

TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = not DEBUG
# ######### END DEBUG CONFIGURATION

config = ConfigIni(PROJECT_DIR.child('infra_confs')+'/settings.ini')

# #########  MAILTRAP CONFIGURATION

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

# #########  END MAILTRAP CONFIGURATION

# ######### EMAIL CONFIGURATION
# EMAIL_HOST = "localhost"
# EMAIL_PORT = 1025
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# ######### END EMAIL CONFIGURATION

# ######### DATABASE CONFIGURATION
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }

# DATABASES = {
#   'default': {
#   'ENGINE': 'django.db.backends.postgresql',
#   'NAME': 'emitir2',
#   'USER': 'postgres',
#   'PASSWORD': 'postgres',
#   'HOST': 'localhost',
#   'PORT': 5432
#    }
#}
# ######### END DATABASE CONFIGURATION
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'me-api.db'),
    }
}

os.environ['REUSE_DB'] = "1"
SOUTH_TESTS_MIGRATE = False
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
TEST_DISCOVER_ROOT = PROJECT_DIR
TEST_DISCOVER_PATTERN = "test_*"

# ######### CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# ######### END CACHE CONFIGURATION


# ######### INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'debug_toolbar',
    'django_nose',
)

# IPs allowed to see django-debug-toolbar output.
INTERNAL_IPS = ("127.0.0.1",)


MIDDLEWARE_CLASSES += \
    ("debug_toolbar.middleware.DebugToolbarMiddleware", )


DEBUG_TOOLBAR_CONFIG = {
    # If set to True (default), the debug toolbar will show an intermediate
    # page upon redirect so you can view any debug information prior to
    # redirecting. This page will provide a link to the redirect
    # destination
    # you can follow when ready. If set to False, redirects will proceed as
    # normal.
    'INTERCEPT_REDIRECTS': False,


    # An array of custom signals that might be in your project, defined as
    # the
    # python path to the signal.
    'EXTRA_SIGNALS': [],


    # If set to True (the default) then a template's context will be
    # included
    # with it in the Template debug panel. Turning this off is useful when
    # you
    # have large template contexts, or you have template contexts with lazy
    # datastructures that you don't want to be evaluated.
    'SHOW_TEMPLATE_CONTEXT': True,

}
# ######### END DJANGO-DEBUG-TOOLBAR CONFIGURATION

RAVEN_CONFIG = {
    'dsn': ''
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'sqlhandler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sqlformatter'
        }
    },
    'formatters': {
        'sqlformatter': {
            '()': 'sqlformatter.SqlFormatter',
            'format': '%(levelname)s %(message)s',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'sqlhandler', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['sentry'],
            'propagate': True,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['sentry'],
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['console'],
            'propagate': False
        },
    }
}
