import email

from django.conf import settings as django_settings
from django.utils.encoding import smart_str
from django.core.mail import send_mail
from django.test import TestCase

import django_smtp_ntlm_backend
from django_smtp_ntlm_backend import settings
from smtplib import SMTP

class FakeSmtpConnection(object):
    outbox = []

    def __init__(self, *args, **kwargs):
        pass

    def sendmail(self, *args, **kwargs):
        self.outbox.append(args)
        pass

    def ehlo(self, **kwargs):
        pass

    def quit(self, **kwargs):
        pass


def fake_ntlm_authenticate(*args, **kwargs):
    pass

class NtlmBackendTest(TestCase):
    def setUp(self):
        django_settings.EMAIL_BACKEND = 'django_smtp_ntlm_backend.NTLMEmail'
        django_smtp_ntlm_backend.SMTP = FakeSmtpConnection
        django_smtp_ntlm_backend.ntlm_authenticate = fake_ntlm_authenticate
        self.outbox = FakeSmtpConnection.outbox

    def test_send_mail(self):
        send_mail('subject', 'body', 'from@example.com', ['to@example.com'])
        message = self.outbox.pop()
        mail = email.message_from_string(smart_str(message[2]))
        self.assertEqual(mail['subject'], 'subject')
        self.assertEqual(mail['from'], 'from@example.com')
        self.assertEqual(mail['to'], 'to@example.com')
        self.assertEqual(mail.get_payload(), 'body')
