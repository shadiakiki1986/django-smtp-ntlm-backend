define VERSION_SCRIPT
from django.conf import settings; settings.configure()
from django_smtp_ntlm_backend import __version__; print(__version__)
endef

VERSION := $(shell python -c '$(VERSION_SCRIPT)')
COMMIT_STATUS := $(shell git commit --porcelain)

release:
ifeq (,${COMMIT_STATUS})
	python setup.py sdist bdist_wheel upload
	ifeq (0,${?})
		@echo "publishing to pypi was ok"
		git tag $(VERSION)
		git push
	else
		@echo "Failed to publish to pypi"
	endif
else	
	@echo "You have uncommited chnages"
endif
