from django.conf import settings

__all__ = ('EMAIL_HOST', 'EMAIL_PORT', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'EMAIL_USE_TLS', 'EMAIL_USE_SSL', 'EMAIL_TIMEOUT', 'EMAIL_SSL_KEYFILE', 'EMAIL_SSL_CERTFILE', 'DEFAULT_CHARSET')


EMAIL_HOST = getattr(settings, 'EMAIL_HOST', None)
EMAIL_PORT = getattr(settings, 'EMAIL_PORT', None)
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = getattr(settings, 'EMAIL_HOST_PASSWORD', None)
EMAIL_USE_TLS = getattr(settings, 'EMAIL_USE_TLS', None)
EMAIL_USE_SSL = getattr(settings, 'EMAIL_USE_SSL', None)
EMAIL_TIMEOUT = getattr(settings, 'EMAIL_TIMEOUT', None)
EMAIL_SSL_KEYFILE = getattr(settings, 'EMAIL_SSL_KEYFILE', None)
EMAIL_SSL_CERTFILE = getattr(settings, 'EMAIL_SSL_CERTFILE', None)
DEFAULT_CHARSET = getattr(settings, 'DEFAULT_CHARSET', None)
