import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.base')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html