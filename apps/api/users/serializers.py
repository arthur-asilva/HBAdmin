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
                'created_at',
                'description',
                'availability'
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
        

class AttendanceSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(source='enrollment.student.id')
    student_name = serializers.CharField(source='enrollment.student.name')

    class Meta:
        model = models.AttendenceList
        fields = [
                'id',
                'date',
                'student_id',
                'student_name',
                'details'
            ]