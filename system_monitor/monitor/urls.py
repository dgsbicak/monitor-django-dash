from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from monitor import views


urlpatterns = [
    path('machine/', views.MachineList.as_view()),
    path('machine/<int:pk>', views.MachineDetail.as_view()),
    path('machineinfo/', views.MachineInfoList.as_view()),
    path('machineinfo/<int:pk>', views.MachineInfoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)