from system_monitor import celery_app

celery_app.autodiscover_tasks()

@celery_app.task
def divide(x,y):
    return x/y