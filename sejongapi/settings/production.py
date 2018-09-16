from sejongapi.settings.base import *

import django_heroku


DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True

REST_FRAMEWORK += {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

django_heroku.settings(locals())
