"""
This code provides a mechanism for running django_smtp_ntlm's internal
test suite without having a full Django project.  It sets up the
global configuration, then dispatches out to `call_command` to
kick off the test suite.

## The Code
"""

# Setup and configure the minimal settings necessary to
# run the test suite.  Note that Django requires that the
# `DATABASES` value be present and configured in order to
# do anything.

import sys
from django.conf import settings

settings.configure(
    INSTALLED_APPS=['django_smtp_ntlm_backend'],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
#    ROOT_URLCONF='django_smtp_ntlm_backend.tests.test_urls',
)

# https://github.com/django-ses/django-ses/blob/master/runtests.py#L34
import django
django.setup()

# Start the test suite now that the settings are configured.
from django.core.management import call_command
call_command("test", "django_smtp_ntlm_backend")
