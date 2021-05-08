from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Machine(models.Model):
    class MachineType(models.TextChoices):
        ANY="ANY", _("Any"),
        DESKTOP = "DT", _("Desktop"),
        CLOUDSERVER = "CS", _('Cloud Server')
        SINGLE_BOARD_COMPUTERS = "SBC", _('Single Board')
    created = models.DateTimeField(auto_now_add=True)
    machinename = models.CharField(max_length=100, blank=False, unique=True)
    machineid = models.IntegerField(null=False, unique=True)
    hasgpu = models.BooleanField(default=False)
    machinetype = models.CharField(
        max_length=5,
        choices=MachineType.choices,
        default=MachineType.ANY)
    def is_tangible(self):
        return self.machinetype in {
            MachineType.DESKTOP, 
            MachineType.SINGLE_BOARD_COMPUTERS
            }
    def is_recent(self):
        return True
    def has_gpu(self):
        return self.hasgpu is True


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

