from rest_framework import serializers
from apps.users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
                'id',
                'name',
                'email',
                'access_group',
                'skills',
                'is_active',
                'photo',
                'created_at'
            ]
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
                'id',
                'name',
                'email',
                'access_group',
                'is_active',
                'photo',
                'created_at',
                'height',
                'mass',
                'workout_tips',
                'born_date',
                'last_access'
            ]