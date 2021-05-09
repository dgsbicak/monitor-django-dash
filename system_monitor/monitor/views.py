from monitor.models import Machine, MachineInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required(login_url="/accounts/login/")
def home_view(request):
    return render(request, "home.html")




