from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from .models import Machine, MachineInfo
from .serializers import MachineSerializer, MachineInfoSerializer, UserSerializer
from .forms import GenerateRandomMachineForm
from .tasks import create_random_machine, send_mail_no_space_left
from utils import logger, disk_space_filled

class GenerateRandomMachineView(FormView):
    template_name = "tasks/generate_random_machine.html"
    form_class = GenerateRandomMachineForm
    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_machine.delay(total)
        return redirect("/app/api/machine")


@login_required(login_url="/app/accounts/login/")
def home_view(request):
    return render(request, "home.html")


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MachineList(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MachineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "machinename"

class MachineInfoList(generics.ListCreateAPIView):
    queryset = MachineInfo.objects.all()
    serializer_class = MachineInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        data = self.request.data
        spaceleft = float( data.get("diskspaceleft") )
        machine_name = Machine.objects.get(pk=data["machine"]).machinename
        is_filled = disk_space_filled(spaceleft)
        # send mail via celery
        if is_filled:
            send_mail_no_space_left.delay(machine_name, spaceleft)


class MachineInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MachineInfo.objects.all()
    serializer_class = MachineInfoSerializer
    permission_classes = [permissions.IsAuthenticated]