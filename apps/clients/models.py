from django.db import models
from apps.users.models import Teacher, Student



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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    teacher = models.ForeignKey('users.Teacher', related_name='teacher', on_delete=models.PROTECT)
    service = models.CharField(max_length=250)
    duration = models.IntegerField(default=1, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    @classmethod
    def create(cls, request):

        data = {
            'client': Client.objects.get(id=request['client']),
            'schedule': request['schedule'],
            'weekday': request['weekday'],
            'price': request['price'].replace(',', '.'),
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
            'price': request['price'].replace(',', '.'),
            'teacher': Teacher.objects.get(id=request['teacher']),
            'service': request['service'],
            'is_active': request.get('is_active', None) is not None
        }
        
        cls.objects.filter(id=id).update(**data)





class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='student', on_delete=models.PROTECT)
    enrollment_class = models.ForeignKey(Classes, related_name='enrollment_class', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)