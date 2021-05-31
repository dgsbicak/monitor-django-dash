from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.test import Client

from monitor_api.models import Machine, MachineInfo, User



class ReadUserTest(APITestCase):
    def setUp(self):
        su = User.objects.create_superuser(
            username="testuser",
            password="testpass",
            email="example@mail.com",
            first_name="test",
            last_name="user"
        )
        self.client.login(username="testuser", password="testpass")

    def test_api_view_machine(self):
        response = self.client.get(reverse("monitor_api:listmachine"), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_view_machineinfo(self):
        response = self.client.get(reverse("monitor_api:listmacinfo"), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateMachineTest(APITestCase):
    def setUp(self):
        su = User.objects.create_superuser(
            username="testuser",
            password="testpass",
            email="example@mail.com",
            first_name="test",
            last_name="user"
        )
        self.client.login(username="testuser", password="testpass")

    def test_api_create_machine_and_machine_info(self):
        # Create Machine
        machine = {
            "machinename":"DESKTOP01Y",
            "machineid":10001,
            "hasgpu":True,
            "machinetype":"DT"
        }
        response = self.client.post(reverse("monitor_api:listmachine"), machine, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create Machine Info
        machineinfo = {
            "machine":"DESKTOP01Y",
            "cpuutil":0.1,
            "cpumem":0.1,
            "diskspaceleft":0.1,
            "disk_r":300,
            "disk_w":0,
            "running":True
        }
        response = self.client.post(reverse("monitor_api:listmacinfo"), machineinfo, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateMachineTest(APITestCase):
    def setUp(self):
        su = User.objects.create_superuser(
            username="testuser",
            password="testpass",
            email="example@mail.com",
            first_name="test",
            last_name="user"
        )
        # Insert Machine
        self.M = Machine.objects.create(
            machinename="DESKTOP-09", machineid=10000, hasgpu=True, machinetype="DT"
        )
        self.client.login(username="testuser", password="testpass")
    
    def test_api_update_machine(self):
        machine = {
            "machinename":"DESKTOP-55",
            "machineid":10001,
            "hasgpu":True,
            "machinetype":"DT"
        }
        response = self.client.put(
            reverse("monitor_api:detailmachine", args=[self.M.machinename]),
            machine
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class DeleteMachineTest(APITestCase):
    def setUp(self):
        su = User.objects.create_superuser(
            username="testuser",
            password="testpass",
            email="example@mail.com",
            first_name="test",
            last_name="user"
        )
        # Insert Machine
        self.M = Machine.objects.create(
            machinename="DESKTOP-09", machineid=10000, hasgpu=True, machinetype="DT"
        )
        self.client.login(username="testuser", password="testpass")

    def test_api_delete_machine(self):
        response = self.client.delete(
            reverse("monitor_api:detailmachine", args=[self.M.machinename])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


