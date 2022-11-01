from rest_framework import serializers
from .models import CAMERA, TEMPERATURE, HUMIDITY, REMNANT_W


class CAMERASerializer(serializers.ModelSerializer):
    class Meta:
        model = CAMERA
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class TEMPERATURESerializer(serializers.ModelSerializer):
    class Meta:
        model = TEMPERATURE
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class HUMIDITYSerializer(serializers.ModelSerializer):
    class Meta:
        model = HUMIDITY
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class REMNANT_WSerializer(serializers.ModelSerializer):
    class Meta:
        model = REMNANT_W
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1
