from django.test import TestCase
from django.contrib.auth.models import User
from monitor.models import Machine, MachineInfo


class TestCreateMachine(TestCase):
    @classmethod
    def setUpTestData(cls):
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


