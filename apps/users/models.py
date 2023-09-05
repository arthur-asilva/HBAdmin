from django.db import models
from django.utils import timezone

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

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
    photo = models.TextField(default='...')
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
            'access_group': 'ADM',
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)
        sendmail(data)

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
    skills = models.JSONField(default=dict)
    description = models.TextField(blank=True, null=True)
    availability = models.JSONField(default=dict)
    is_hired = models.BooleanField(default=True, blank=True, null=True)

    @classmethod
    def create(cls, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'password': get_random_string(6),
            'access_group': 'PRO',
            'skills': {'services': request.getlist('services')},
            'availability': {'availabilities': request.getlist('availabilities')},
            'description': request['description'],
            'is_hired': request.get('is_hired', None) is not None,
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)
        sendmail(data)

    @classmethod
    def update(cls, id, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'skills': {'services': request.getlist('services')},
            'availability': {'availabilities': request.getlist('availabilities')},
            'description': request['description'],
            'is_hired': request.get('is_hired', None) is not None,
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)

    def __str__(self):
        return self.name





def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str





class Student(User):
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    mass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    workout_tips = models.JSONField(default=dict)
    born_date = models.DateField(null=True, blank=True, default=None)
    last_access = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls, request):

        data = {
            'name': request['name'],
            'email': request['email'],
            'password': get_random_string(6),
            'access_group': 'ALU',
            'is_active': request.get('is_active', None) is not None
        }

        cls.objects.create(**data)
        sendmail(data)

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





class AttendenceList(models.Model):

    ATTENDANCE_STATUS = [
        (0, 'Presente'),
        (1, 'Falta'),
        (2, 'Justificado'),
        (3, 'Reagendado')
    ]

    # enrollment = models.ForeignKey('clients.Enrollment', related_name='enrollment', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    enrollments = models.JSONField(default={'enrollments': []})
    attendence_class = models.ForeignKey('clients.Classes', related_name='attendence_class', on_delete=models.PROTECT, null=True)
    details = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    total_likes = models.IntegerField(default=0)
    likes = models.JSONField(default={'users': []})
    # status = models.IntegerField(choices=ATTENDANCE_STATUS)





class Token(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=8)
    created_at = models.DateField(default=timezone.now())





def sendmail(user):
    
    ctx = {
        'name': user['name'],
        'password': user['password'],
        'email': user['email']
    }

    message = get_template('users/on_create_email.html').render(ctx)
    msg = EmailMessage('HealthyBody', message, 'icaro.arthur66@gmail.com', [user['email']])
    msg.content_subtype ="html"
    msg.send()

    print("Mail successfully sent")