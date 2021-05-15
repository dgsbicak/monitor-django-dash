from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from monitor.models import Machine, MachineInfo

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
        machineinfo =     {
            "machine": 1,
            "cpuutil": 0.1,
            "cpumem": 0.1,
            "diskspaceleft": 0.1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)