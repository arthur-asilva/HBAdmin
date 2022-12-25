from django.db import models
from django.utils import timezone
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
