from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return self.name

