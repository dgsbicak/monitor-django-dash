from django.utils.crypto import get_random_string
from random import randint
from celery import shared_task
import os
from django.core.mail import send_mail

from system_monitor import celery_app
from .models import Machine
from utils import logger

@shared_task
def create_random_machine(total):
    for i in range(total):
        data = {"machinename":get_random_string(10),
            "machineid":randint(1000,9999),
            "hasgpu":bool(randint(0,1))}
        Machine.objects.create(**data)
    return "{} Random machines created with success!".format(total)

@shared_task
def send_mail_no_space_left(machine_name, diskspaceleft):
    send_mail(
        'ALARM MAIL',
        f'{diskspaceleft} mb space left in the machine: {machine_name}!',
        os.environ.get("MAIL_FROM"),
        os.environ.get("MAIL_TO").split(),
        fail_silently=False,
    )
    logger.warning("Alarm mail sent to {}".format(os.environ.get("MAIL_TO")))

