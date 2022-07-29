#!/bin/bash
python manage.py migrate --noinput
exec gunicorn -c "gunicorn_config.py" insta_api.wsgi