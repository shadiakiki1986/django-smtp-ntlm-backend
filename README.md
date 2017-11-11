# django-smtp-ntlm-backend
Django email backend supporting SMTP with NTLM authentication, e.g. for MS Outlook Exchange over SMTP

Mostly copied from
- https://www.pythondiary.com/tutorials/django-ntlm-smtp-auth.html
- [piotrbulinski/django-ses-backend](https://github.com/piotrbulinski/django-ses-backend)
- [django-ses](https://github.com/django-ses/django-ses)

License same as [python-ntlm3](https://github.com/trustrachel/python-ntlm3/blob/master/LICENSE.md)

# Installing

`pip install django-smtp-ntlm-backend`

and until https://github.com/trustrachel/python-ntlm3/pull/24 is closed

`pip install git+https://github.com/shadiakiki1986/python-ntlm3.git@feature_smtp`

and add the settings variables for SMTP as usual, with the username being `domain\\user`

# Testing
```bash
pew new DJANGO_SMTP_NTLM
pip3 install -q Django==1.11
pip3 install -r requirements.txt
python3 runtests.py
```

# Usage

In the `settings.py`, use

    EMAIL_BACKEND = 'django_smtp_ntlm_backend.NTLMEmail'
    EMAIL_HOST = "mail.server.com"
    EMAIL_PORT = port # e.g. 587
    EMAIL_HOST_USER = "domain\\username"
    EMAIL_HOST_PASSWORD = "password"
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = False
    DEFAULT_FROM_EMAIL="Someone <from@email.com>"


# Publishing to pypi
Run
```bash
pew in DJANGO_SMTP_NTLM make release
```

If your username/password for pypi are not in a `.pypirc` file ([ref](http://peterdowns.com/posts/first-time-with-pypi.html)),
you will be prompted to type in your credentials.
