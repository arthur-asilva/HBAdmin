from rest_framework import serializers
from apps.clients import models

class ClassSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(source='client.name')
    client_address = serializers.CharField(source='client.address')

    class Meta:
        model = models.Classes
        fields = [
                'client',
                'client_name',
                'client_address',
                'schedule',
                'weekday',
                'price',
                'teacher',
                'service',
                'is_active'
            ]