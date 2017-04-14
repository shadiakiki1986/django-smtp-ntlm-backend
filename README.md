# django-smtp-ntlm-backend
Django email backend supporting SMTP with NTLM authentication

Mostly copied from
- https://www.pythondiary.com/tutorials/django-ntlm-smtp-auth.html
- [piotrbulinski/django-ses-backend](https://github.com/piotrbulinski/django-ses-backend)
- [django-ses](https://github.com/django-ses/django-ses)

License same as [python-ntlm3](https://github.com/trustrachel/python-ntlm3/blob/master/LICENSE.md)

# Testing
```bash
pew new DJANGO_SMTP_NTLM
pip3 install -q Django==1.11
pip3 install -r requirements.txt
python3 runtests.py
```

# Publishing to pypi
Run
```bash
pew in DJANGO_SMTP_NTLM make release
```

If your username/password for pypi are not in a `.pypirc` file ([ref](http://peterdowns.com/posts/first-time-with-pypi.html)),
you will be prompted to type in your credentials.
