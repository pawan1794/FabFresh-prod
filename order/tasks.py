from FabFresh._celery import app as celery

@celery.task
def add(x, y):
    return x + y