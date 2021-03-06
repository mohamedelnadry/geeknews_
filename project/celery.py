from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "scheduled_task": {
        "task": "scraper.tasks.get_data",
        "schedule": crontab(minute=0, hour=0),
        # 'args': (16, 16)
    },
}

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))