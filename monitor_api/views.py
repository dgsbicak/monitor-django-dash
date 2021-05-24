from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.views.generic.edit import FormView

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from .models import Machine, MachineInfo
from .serializers import MachineSerializer, MachineInfoSerializer
from .forms import GenerateRandomMachineForm, UserCreationForm
from monitor_api.utils.tasks import create_random_machine, send_mail_no_space_left
from utils import logger, disk_space_filled


def signup(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    elif request.method=="GET":
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})


class GenerateRandomMachineView(FormView):
    template_name = "tasks/generate_random_machine.html"
    form_class = GenerateRandomMachineForm
    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_machine.delay(total) # task
        return redirect("/app/api/machine")


@login_required(login_url="/app/accounts/login/")
def home_view(request):
    return render(request, "home.html")


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