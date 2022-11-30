from __future__ import absolute_import , unicode_literals
from django.conf import settings
import os
from celery import Celery
from celery.schedules import crontab




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


app.config_from_object(settings , namespace='CELERY')


"""
Note : the name of the task should be unique: for example
in our case , you should not add another task of name "send_mail_everyday_at_12".
If you do so you will receive a unique constrain error
"""
# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send_mail_everyday_at_12':{
        'task':'client.tasks.client_mail',
        'schedule': crontab(hour=10, minute=16), 
        # 'args': () 
    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')