from django.shortcuts import render
from django.http import HttpResponse
from .tasks import client_mail
from django_celery_beat.models import PeriodicTask , CrontabSchedule
# Create your views here.


def home(request):
    client_mail.delay()
    return HttpResponse('DONE')

def index(request):
    schedule , created = CrontabSchedule.objects.get_or_create(hour=10 , minute=34) 
    """
    Dont forget that task name must be unique.
    You can also add argument to the object. If args is added you must add the arg in the task function
    """
    task = PeriodicTask.objects.create(crontab=schedule, name='random_name', task='client.tasks.client_mail')
    return HttpResponse('DONE')