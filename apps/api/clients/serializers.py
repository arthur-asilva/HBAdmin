from rest_framework import serializers
from apps.clients import models

class ClassSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(source='client.name')
    client_address = serializers.CharField(source='client.address')

    class Meta:
        model = models.Classes
        fields = [
                'id',
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




class EnrollmentSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(source='student.id')
    student_name = serializers.CharField(source='student.name')
    class_name = serializers.CharField(source='enrollment_class.client.name')
    class_schedule = serializers.CharField(source='enrollment_class.schedule')
    class_weekday = serializers.CharField(source='enrollment_class.weekday')

    class Meta:
        model = models.Enrollment
        fields = [
                    'id',
                    'student_id',
                    'student_name',
                    'class_name',
                    'class_schedule',
                    'class_weekday'
            ]