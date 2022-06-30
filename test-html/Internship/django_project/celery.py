from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule= {
    'import_TLE_1min':{
        'task':'pages.tasks.importTLE',
        'schedule': 1800.0
    }
}



app.autodiscover_tasks()
