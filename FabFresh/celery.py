from __future__ import absolute_import
import os
import celery
print celery.__file__
from celery import Celery
from django.conf import settings

app = Celery('fabfresh', broker='amqp://hari:hari@52.48.75.63:5672/fabfresh')
#app = Celery('fabfresh',broker='amqp://guest@localhost//')

@app.task()
def add(x, y):
    return x + y
