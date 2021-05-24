from django.db.models.signals import post_delete
from django.dispatch import receiver

from monitor_api.models import Machine, MachineInfo
from utils import logger

@receiver(post_delete, sender=Machine)
def machine_delete_check(sender, **kwargs):
    logger.warning(f"Machine deleted!: {str(kwargs['instance'])}")
    # Do Something
    # -->