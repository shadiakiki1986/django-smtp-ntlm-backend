# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


DESCRIPTION = "A Django email backend for SMTP servers with NTLM authentication"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-smtp-ntlm-backend',
    version='0.0.4',  # When changing this, remember to change it in __init__.py
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['django_smtp_ntlm_backend'],
    author='Shadi Akiki',
    author_email='shadiakiki1986@gmail.com',
    maintainer='Shadi Akiki',
    maintainer_email='shadiakiki1986@gmail.com',
    url='https://github.com/shadiakiki1986/django-smtp-ntlm-backend/',
    download_url='https://github.com/shadiakiki1986/django-smtp-ntlm-backend/archive/master.zip',
    license='GNU Lesser GPL',
    platforms=['Posix', 'MacOS X', 'Windows'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django >= 1.5',
        # until https://github.com/trustrachel/python-ntlm3/pull/24
        # is closed, using my own published pypi package
        # from my own github fork
        'shadiakiki1986-python-ntlm3 >= 1.0.5-dev'
    ],
)
