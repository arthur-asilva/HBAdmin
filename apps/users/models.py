from django.db import models
from django.utils import timezone
from apps.clients.models import Classes
import random
import string




class User(models.Model):

    ACCESS_GROUPS = [
        ('ADM', 'Administrador'),
        ('PRO', 'Professor'),
        ('ALU', 'Aluno')
    ]

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    photo = models.CharField(max_length=250, default='...')
    password = models.CharField(max_length=250)
    access_group = models.CharField(max_length=3, choices=ACCESS_GROUPS)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        abstract = True





class Administrator(User):

    @classmethod
    def create(cls, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'password': get_random_string(6),
            'access_group': 'Administrador',
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)

    @classmethod
    def update(cls, id, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)

    def __str__(self):
        return self.name





class Teacher(User):
    skills = models.JSONField(default={})

    @classmethod
    def create(cls, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'password': get_random_string(6),
            'access_group': 'Professor',
            'skills': {'services': request.getlist('services')},
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)

    @classmethod
    def update(cls, id, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'skills': {'services': request.getlist('services')},
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)

    def __str__(self):
        return self.name





def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str





# class Student(User):
#     height = models.DecimalField(max_digits=3, decimal_places=2)
#     mass = models.DecimalField(max_digits=5, decimal_places=2)
#     workout_tips = models.JSONField(default={})
#     born_date = models.DateField(null=True, blank=True)
#     last_access = models.DateField(default=timezone.now())

#     def __str__(self):
#         return self.name





# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, related_name='student', on_delete=models.PROTECT)
#     enrollment_class = models.ForeignKey(Classes, related_name='class', on_delete=models.PROTECT)
#     is_active = models.BooleanField(default=True)





# class AttendenceList(models.Model):

#     ATTENDANCE_STATUS = [
#         (0, 'Present'),
#         (1, 'Absent'),
#         (2, 'Justificado'),
#         (3, 'Reagendado')
#     ]

#     enrollment = models.ForeignKey(Enrollment, related_name='enrollment', on_delete=models.PROTECT)
#     date = models.DateField(default=timezone.now())
#     status = models.IntegerField(choices=ATTENDANCE_STATUS)