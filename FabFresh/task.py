#import os
from celery import Celery
import requests

import json
from rest_framework import status
#from rest_framework.response import Response



app = Celery('fabfresh', broker='amqp://hari:hari@52.48.75.63:5672/fabfresh')
#app = Celery('fabfresh',backend='redis://',broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    if x+y == 4:
        add.retry()
    return x + y

@app.task
def text(phone,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)
    print r1

@app.task
def serviceAv(payload):
    url = 'http://roadrunnr.in/v1/orders/serviceability'
    headers = {'Authorization' : 'Bearer L0vqwtrFUodi6VA8HhxKtSdVjTinUUaoHEUk2VPP' , 'Content-Type' : 'application/json'}
    try:
        r = requests.post(url, json.dumps(payload), headers=headers)
    except Exception as e:
        serviceAv.retry()
    #response = Response(r.json(),status=status.HTTP_200_OK)
    print r.json()
    if len(r.json()) < 4 :
        result = serviceAv.retry(countdown=5,max_retries=10)
        print result.status
        print "asd"
    else:
        text.delay("7204680605","Delivery boy available, you can make your order now")
