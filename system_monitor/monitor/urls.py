from django.urls import path
from django.views.generic import TemplateView


app_name = 'monitor'

urlpatterns = [
    path('', TemplateView.as_view(template_name="monitor/index.html")),
]