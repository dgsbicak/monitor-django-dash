from monitor.models import Machine, MachineInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import GenerateRandomMachineForm
from .tasks import create_random_machine


class GenerateRandomMachineView(FormView):
    template_name = "tasks/generate_random_machine.html"
    form_class = GenerateRandomMachineForm
    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_machine.delay(total)
        messages.success(self.request, 
            "We are generating your random machines! Wait a moment and refresh this page.")
        return redirect("/api/machine")


@login_required(login_url="/accounts/login/")
def home_view(request):
    return render(request, "home.html")





