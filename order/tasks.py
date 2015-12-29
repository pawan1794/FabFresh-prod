from FabFresh.task import app as celery

@celery.task
def add(x, y):
    return x + y