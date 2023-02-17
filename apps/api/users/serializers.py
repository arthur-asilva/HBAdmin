from rest_framework import serializers
from apps.users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
                'id',
                'name',
                'email',
                'password',
                'access_group',
                'skills',
                'is_active'
            ]