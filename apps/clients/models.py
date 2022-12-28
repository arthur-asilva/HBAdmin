from django.db import models
from apps.users.models import Teacher



class Service(models.Model):
    name = models.CharField(max_length=250)


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    services = models.JSONField(default={})
    is_active = models.BooleanField(default=True)

    @classmethod
    def create(cls, request):

        data = {
            'name': request['name'],
            'address': request['address'],
            'services': {'services': request.getlist('services')},
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)

    @classmethod
    def update(cls, id, request):

        data = {
            'name': request['name'],
            'address': request['address'],
            'services': {'services': request.getlist('services')},
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)





class Classes(models.Model):

    WEEKDAY_CHOICES = [
        (0, 'Segunda'),
        (1, 'Terça'),
        (2, 'Quarta'),
        (3, 'Quinta'),
        (4, 'Sexta'),
        (5, 'Sábado'),
        (6, 'Domingo')
    ]

    client = models.ForeignKey(Client, related_name='client', on_delete=models.PROTECT)
    schedule = models.CharField(max_length=5)
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES)
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.PROTECT)
    service = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    @classmethod
    def create(cls, request):

        data = {
            'client': Client.objects.get(id=request['client']),
            'schedule': request['schedule'],
            'weekday': request['weekday'],
            'teacher': Teacher.objects.get(id=request['teacher']),
            'service': request['service'],
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.create(**data)

    @classmethod
    def update(cls, id, request):

        data = {
            'client': Client.objects.get(id=request['client']),
            'schedule': request['schedule'],
            'weekday': request['weekday'],
            'teacher': Teacher.objects.get(id=request['teacher']),
            'service': request['service'],
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)
