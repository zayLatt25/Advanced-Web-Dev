from rest_framework import serializers
from .models import SavedSelections, UserProfile, Case, CpuCooler, Cpu, InternalHardDrive, Memory, Motherboard, GPU, PowerSupply
from django.utils.functional import SimpleLazyObject

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CpuCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuCooler
        fields = '__all__'

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class InternalHardDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalHardDrive
        fields = '__all__'

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupply
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'

class SavedSelectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSelections
        fields = '__all__'
        read_only_fields = ['user']  

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)