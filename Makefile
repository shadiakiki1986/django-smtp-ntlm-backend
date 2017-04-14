define VERSION_SCRIPT
from django.conf import settings; settings.configure()
from django_smtp_ntlm_backend import __version__; print(__version__)
endef

VERSION := $(shell python -c '$(VERSION_SCRIPT)')
COMMIT_STATUS := $(shell git commit --porcelain)

release:
ifeq (,${COMMIT_STATUS})
	# use "-r pypitest" after "upload" below to submit to test pypi server
	python setup.py sdist bdist_wheel upload || ( echo "Failed to publish to pypi"; exit 1 )
	git tag $(VERSION)
	git push
else	
	@echo "You have uncommited chnages"
endif
