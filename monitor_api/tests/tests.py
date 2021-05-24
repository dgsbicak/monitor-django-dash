from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from monitor_api.models import Machine, MachineInfo, User


class PostTests(APITestCase):

    def test_view_machine(self):
        testuser1 = User.objects.create_user(username="test_user1", password="testuser")
        url = reverse("monitor_api:listmachine")
        self.assertEqual(self.client.login(username="test_user1", password="testuser"), True)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_machine_info(self):
        testuser1 = User.objects.create_user(username="test_user1", password="testuser")
        self.assertEqual(self.client.login(username="test_user1", password="testuser"), True)
        url = reverse("monitor_api:listmachine")
        machineinfo = {
            "machine": 1,
            "cpuutil": 0.1,
            "cpumem": 0.1,
            "diskspaceleft": 0.1,
        }
        response = self.client.post(url, machineinfo, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class TestCreateMachine(TestCase):
    @classmethod
    def setUp(cls):
        test_machine = Machine.objects.create(machinename="cloud77",
             machineid=1077, hasgpu=False, machinetype="CS")
        testuser1 = User.objects.create_user(username="test_user1", password="testuser")
        test_info = MachineInfo.objects.create(machine=test_machine, cpuutil=0.7, cpumem=0.3, 
            diskspaceleft=0.2, internet_access=False, running=True)
    
    def test_machine_info(self):
        machine = Machine.objects.get(id=1)
        mname = f'{machine.machinename}'
        mgpu = machine.hasgpu
        mtype = f'{machine.machinetype}'
        info = MachineInfo.todaysobjects.get(id=1)
        cpuinfo = info.cpuutil
        self.assertEqual(str(machine), "cloud77")
        self.assertEqual(mname, "cloud77")
        self.assertEqual(mgpu, machine.has_gpu())
        self.assertEqual(mtype, "CS")
        self.assertEqual(cpuinfo, 0.7)
        self.assertEqual(info.is_recent(), True)


