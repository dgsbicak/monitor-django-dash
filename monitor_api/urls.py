from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from .views import GenerateRandomMachineView
from monitor_api import views

app_name = 'monitor_api'

urlpatterns = [
    path('machine/', views.MachineList.as_view(), name='listmachine'),
    path('machine/<str:machinename>', views.MachineDetail.as_view(), name='detailmachine'),
    path('machineinfo/', views.MachineInfoList.as_view(), name='listmacinfo'),
    path('machineinfo/<int:pk>', views.MachineInfoDetail.as_view(), name='detailmacinfo'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('generate/', GenerateRandomMachineView.as_view(), name="generate"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += staticfiles_urlpatterns()