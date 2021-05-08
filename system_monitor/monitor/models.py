from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Machine(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    machinename = models.CharField(max_length=100, blank=False)
    machineid = models.IntegerField(null=False)
    class MachineType(models.TextChoices):
        ANY="ANY", _("Any"),
        DESKTOP = "DT", _("Desktop"),
        CLOUDSERVER = "CS", _('Cloud Server')
        SINGLE_BOARD_COMPUTERS = "SBC", _('Single Board')
    machinetype = models.CharField(
        max_length=5,
        choices=MachineType.choices,
        default=MachineType.ANY)
    def is_defined(self):
        return self.machinetype in {
            MachineType.DESKTOP, 
            MachineType.CLOUDSERVER, 
            MachineType.SINGLE_BOARD_COMPUTERS
            }
    

class MachineInfo(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    cpuutil = models.FloatField()
    cpumem = models.FloatField()
    gpuutil = models.FloatField(null=True)
    gpumem = models.FloatField(null=True)
    diskspaceleft = models.FloatField(null=True)
    disk_r = models.FloatField(null=True)
    disk_w = models.FloatField(null=True)
    network_r = models.FloatField(null=True)
    network_t = models.FloatField(null=True)
    internet_access = models.BooleanField(null=True)
    running = models.BooleanField()

