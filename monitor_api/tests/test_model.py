from django.test import TestCase
from monitor_api.models import Machine, MachineInfo, User


class TestUser(TestCase):

    def test_user_create(self):
        User.objects.create(
            username="testuser",
            password="testpass",
            email="example@mail.com",
            first_name="test",
            last_name="user"
        )

class TestMachine(TestCase):

    def test_create_machine_and_valuecheck(self):
        # Insert Machine
        Machine.objects.create(
            machinename="cloud77",machineid=1077, hasgpu=False, machinetype="CS")
        machine = Machine.objects.get(machinename="cloud77")
        mname = f'{machine.machinename}'
        mtype = f'{machine.machinetype}'
        self.assertEqual(str(machine), "cloud77")
        self.assertEqual(mname, "cloud77")
        self.assertFalse(machine.has_gpu())
        self.assertEqual(mtype, "CS")


class TestMachineInfo(TestCase):

    def test_create_machineinfo_and_valuecheck(self):
        # Insert Machine
        M = Machine.objects.create(
            machinename="cloud77",machineid=1077, hasgpu=False, machinetype="CS")
        # Insert Machine Info 
        MachineInfo.objects.create(
            machine=M, cpuutil=0.7, cpumem=0.3, 
            diskspaceleft=0.2, internet_access=False, running=True)
        info = MachineInfo.todaysobjects.get(machine="cloud77")
        self.assertEqual(info.cpuutil, 0.7)
        self.assertEqual(info.cpumem, 0.3)
        self.assertEqual(info.diskspaceleft, 0.2)
        self.assertFalse(info.internet_access)
        self.assertTrue(info.is_recent(), True)


