#!/bin/bash
exec gunicorn -c "gunicorn_config.py" insta_api.wsgi