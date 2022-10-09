VERSION ?= 3.9-alpine
IMAGE_NAME=game2048-python
IMAGE=${IMAGE_NAME}:${VERSION}

all: build

.PHONY: setup
setup:
	-docker network create game

.PHONY: bump
bump:
	poetry version patch

.PHONY: build
build: setup
	docker build -t ${IMAGE} .
