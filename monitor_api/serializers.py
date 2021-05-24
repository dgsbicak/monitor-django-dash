from rest_framework import serializers

from .models import Machine, MachineInfo



class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ["created", "machinename", "machineid", 
            "hasgpu", "machinetype"]

class MachineInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineInfo
        fields = ["machine","created","cpuutil","cpumem","gpuutil","gpumem","diskspaceleft",
            "disk_r","disk_w","network_r","network_t","internet_access","running",
        ]