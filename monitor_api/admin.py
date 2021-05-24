from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User as AUser

#admin.site.unregister(AUser)
#admin.site.unregister(Group)

# Register your models here.
from .models import Machine, MachineInfo, User




admin.site.register(User, UserAdmin)
admin.site.register(Machine)
admin.site.register(MachineInfo)