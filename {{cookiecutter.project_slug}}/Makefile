SHELL := /bin/bash

VERSION := $(GO_PIPELINE_LABEL)

ifeq ($(strip $(VERSION)),)
  VERSION := latest
endif

define clean-build =
    find . -path '*/__pycache__/*' -delete
    find . -type d -name '__pycache__' -empty -delete
	find . -path '*.egg-info/*' -delete
	find . -type d -path '*.egg-info' -empty -delete
	rm -rf build;
endef

build:
	docker build -t scrapy_{{cookiecutter.project_module}}:${VERSION} .
	docker build -t scrapy_{{cookiecutter.project_module}}:latest .

run:
ifdef SPIDER
	@echo "Você pode especificar a opção SPIDER=<spider name> para rodar um spider específico, ou deixar em branco para rodar todos."
	python3 scripts/run_spider.py --s ${SPIDER}
else
	python3 scripts/run_spider.py
endif

install:
	echo "make install NOT IMPLEMENTED"

release:
	shub deploy
	$(clean-build)

clean-pyc:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name '*~' -delete

clean-build:
	$(clean-build)

uninstall:
	echo "make uninstall NOT IMPLEMENTED"

test:
	echo "make test NOT IMPLEMENTED"

docker-run:
ifdef SPIDER
	@echo "Você pode especificar a opção SPIDER=<spider name> para rodar um spider específico, ou deixar em branco para rodar todos."
	docker run --rm -v ${PWD}/output:/app/output/ --name scrapy_{{cookiecutter.project_module}} --network host scrapy_{{cookiecutter.project_module}} python3 scripts/run_spider.py --s ${SPIDER}
else
	docker run --rm -v ${PWD}/output:/app/output/ --name scrapy_{{cookiecutter.project_module}} --network host scrapy_{{cookiecutter.project_module}} python3 scripts/run_spider.py
endif

docker-build:
	docker build -t scrapy_{{cookiecutter.project_module}}:${VERSION} .
	docker build -t scrapy_{{cookiecutter.project_module}}:latest .

docker-push:
	echo "make docker-push NOT IMPLEMENTED"
