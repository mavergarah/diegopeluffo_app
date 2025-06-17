from .settings_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda self: True
}

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
