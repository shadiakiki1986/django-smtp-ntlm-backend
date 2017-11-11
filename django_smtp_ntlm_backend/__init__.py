from django.core.mail.backends.smtp import EmailBackend
from ntlm3.smtp import ntlm_authenticate
from smtplib import SMTP
from django.core.mail.utils import DNS_NAME

# When changing this, remember to change it in setup.py
VERSION = (0, 0, 4)
__version__ = '.'.join([str(x) for x in VERSION])
__author__ = 'Shadi Akiki'
__all__ = ('SmtpNtlmBackend',)

# Copied from https://www.pythondiary.com/tutorials/django-ntlm-smtp-auth.html
class NTLMEmail(EmailBackend):
  def open(self):
    """
    Ensures we have a connection to the email server. Returns whether or
    not a new connection was required (True or False).
    """
    if self.connection:
      # Nothing to do if the connection is already open.
      return False
    try:
      # If local_hostname is not specified, socket.getfqdn() gets used.
      # For performance, we use the cached FQDN for local_hostname.
      self.connection = SMTP(
        self.host, self.port,
        local_hostname=DNS_NAME.get_fqdn()
      )
      self.connection.ehlo()
      if self.username and self.password:
        ntlm_authenticate(self.connection, self.username, self.password)
      return True
    except:
      if not self.fail_silently:
        raise
