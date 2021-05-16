from django.db.models.signals import post_delete
from django.dispatch import receiver

from monitor_api.models import Machine, MachineInfo
from utils import logger

@receiver(post_delete, sender=Machine)
def check_machine_alarm_state(sender, **kwargs):
    logger.warning(f"Machine deleted!: {str(kwargs['instance'])}")