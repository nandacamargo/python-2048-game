FROM python:3.9-alpine
USER root

WORKDIR /game

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

# Update the image, install python3 pip and poetry and then remove unnecessary cache
RUN apk update && \
    apk add --no-cache py3-pip curl && \
    python3 -m  pip install "poetry==1.1.15" && \
    python3 -m pip install --upgrade pip wheel setuptools && \
    rm -rf /var/cache/apk/*

COPY pyproject.toml ./
# COPY pyproject.toml poetry.lock ./

COPY game/ .
RUN poetry export --without-hashes --dev -o requirements.txt
RUN pip install -r requirements.txt

RUN poetry build
