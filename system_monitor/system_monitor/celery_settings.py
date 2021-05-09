import logging
import os
from celery import Celery

logger = logging.getLogger("celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'system_monitor.settings')

app = Celery('tasks')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task
def add(x,y):
    return x+y