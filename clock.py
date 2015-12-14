from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


import logging
logging.basicConfig()
import requests
def message(phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)


def test():
    print "inside test"
    #message("7204680605","wassup")
    sched.stop()
    print "After message"

#sched = BlockingScheduler()
sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=0.05)
def timed_job():
    test()
    print('This job is run every three minutes.')
'''
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=01)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
'''
sched.start()

