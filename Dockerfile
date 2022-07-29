FROM python:3.8-slim-buster

ENV PIPENV_NOSPIN true
ENV PYTHONUNBUFFERED 1

# install packages
RUN apt-get -y update \
    && apt-get install -y libgdal-dev\
    && apt-get update

# RUN apt-get install -y nginx

RUN mkdir -p /static /media

WORKDIR /app

ARG STATIC_ROOT
ENV STATIC_ROOT ${STATIC_ROOT:-/static/}

ARG MEDIA_ROOT
ENV MEDIA_ROOT ${MEDIA_ROOT:-/media/}

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

# COPY default /etc/nginx/sites-enabled/default

COPY ./setup_gunicorn.sh /setup_gunicorn.sh
RUN chmod +x /setup_gunicorn.sh

RUN python manage.py collectstatic --noinput

CMD ["/setup_gunicorn.sh"]
