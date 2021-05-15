from celery import shared_task
from django.utils.crypto import get_random_string
from random import randint
from system_monitor import celery_app
from .models import Machine

@shared_task
def create_random_machine(total):
    for i in range(total):
        data = {"machinename":get_random_string(10),
            "machineid":randint(1000,9999),
            "hasgpu":bool(randint(0,1))}
        Machine.objects.create(**data)
    return "{} Random machines created with success!".format(total)