from django.urls import path
from django.views.generic import TemplateView
from .views import GenerateRandomMachineView


app_name = 'monitor'

urlpatterns = [
    path('', TemplateView.as_view(template_name="monitor/index.html")),
    path('generate', GenerateRandomMachineView.as_view(), name="generate"),
]