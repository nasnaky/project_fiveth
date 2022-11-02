from rest_framework import serializers
from .models import USER, SERVER


class USERSerializers(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


class SERVERListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SERVER
        fields = ['id', 'TITLE', 'LINK', 'STATUS']
        read_only_fields = ['id', 'STATUS']
        depth = 1


class SERVERCreateSerializers(serializers.ModelSerializer):
    USER = serializers.IntegerField()

    class Meta:
        model = SERVER
        fields = ['id', 'TITLE', 'CENTENT', 'LINK', 'USER']
        depth = 1


class SERVERSerializers(serializers.ModelSerializer):
    class Meta:
        model = SERVER
        fields = ['id', 'TITLE', 'CENTENT', 'LINK']
        read_only_fields = ['id']
        depth = 1
