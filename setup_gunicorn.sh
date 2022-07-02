#!/bin/bash
source venv/bin/activate
exec gunicorn -c "gunicorn_config.py" insta_api.wsgi