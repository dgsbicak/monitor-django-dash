from django.contrib import admin

# Register your models here.
from .models import Machine, MachineInfo


admin.site.register(Machine)
admin.site.register(MachineInfo)