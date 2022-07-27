import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insta_api.settings')

app = Celery('insta_api')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = "Asia/Almaty"
