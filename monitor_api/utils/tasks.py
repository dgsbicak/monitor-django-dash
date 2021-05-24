import os
from random import randint
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from celery import shared_task
from celery.schedules import crontab

from system_monitor import celery_app
from monitor_api.models import Machine, MachineInfo
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


@celery_app.task
def check_stopped_machine_infos():
    try:
        last_machine_infos = map(lambda machine: MachineInfo.objects.filter(machine=machine).last(), Machine.objects.all())
        not_recent_machine_infos = filter(lambda mi: (mi is not None) and (not mi.is_recent()), last_machine_infos)
        not_recent_machine_names = list( map(lambda mi: mi.machine.machinename, not_recent_machine_infos) )
        print(not_recent_machine_names)
        if len(not_recent_machine_names) > 0:
            message = "No info received from the machines within 24 hrs: \n- {}".format(
                "\n- ".join(not_recent_machine_names)
            )
            logger.info(message)
            send_mail(
                'ALARM MAIL',
                message,
                os.environ.get("MAIL_FROM"),
                os.environ.get("MAIL_TO").split(),
                fail_silently=False,
            )
        else:
            logger.info("All machines are running smoothly.")       
    except:
        logger.error(msg="", exc_info=True)

@celery_app.task
def test():
    logger.info("this is a test task!")

