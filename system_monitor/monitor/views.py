from monitor.models import Machine, MachineInfo
from monitor.serializers import MachineSerializer, MachineInfoSerializer, UserSerializer

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions


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

class MachineInfoList(generics.ListCreateAPIView):
    queryset = MachineInfo.objects.all()
    serializer_class = MachineInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

class MachineInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MachineInfo.objects.all()
    serializer_class = MachineInfoSerializer
    permission_classes = [permissions.IsAuthenticated]