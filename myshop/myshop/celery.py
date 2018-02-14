from __future__ import absolute_import
import os
import celery
from celery import Celery
from django.conf import settings

from .settings import INSTALLED_APPS

print celery.__file__

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
