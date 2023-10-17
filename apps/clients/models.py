from django.db import models
from datetime import datetime



class Service(models.Model):
    name = models.CharField(max_length=250)


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    services = models.JSONField(default=dict)
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

    # WEEKDAY_CHOICES = [
    #     (0, 'Segunda'),
    #     (1, 'Terça'),
    #     (2, 'Quarta'),
    #     (3, 'Quinta'),
    #     (4, 'Sexta'),
    #     (5, 'Sábado'),
    #     (6, 'Domingo')
    # ]

    def weekday_default_value():
        return {'days': []}

    client = models.ForeignKey('clients.Client', null=True, related_name='client', on_delete=models.PROTECT)
    schedule = models.CharField(max_length=5)
    weekday = models.JSONField(default=weekday_default_value, blank=True, null=True)
    price = models.DecimalField(max_digits=10, null=True, decimal_places=2, default=0.00)
    teacher = models.ForeignKey('users.Teacher', null=True, related_name='teacher', on_delete=models.PROTECT)
    service = models.CharField(max_length=250)
    duration = models.IntegerField(default=1, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    @classmethod
    def create(cls, request):

        data = {
            'client': request['client'],
            'schedule': request['schedule'],
            'weekday': {"days": [int(x) for x in request.getlist('weekday')]},
            'price': request['price'].replace(',', '.'),
            'teacher': request['teacher'],
            'service': request['service'],
            'duration': request['duration'],
            'is_active': request.get('is_active', None) is not None
        }
        cls.objects.create(**data)

    @classmethod
    def update(cls, id, request):

        data = {
            'client': request['client'],
            'schedule': request['schedule'],
            'weekday': {"days": [int(x) for x in request.getlist('weekday')]},
            'price': request['price'].replace(',', '.'),
            'teacher': request['teacher'],
            'service': request['service'],
            'duration': request['duration'],
            'is_active': request.get('is_active', None) is not None
        }
        cls.objects.filter(id=id).update(**data)





class Notice(models.Model):

    def classes_default_value():
        return {'classes': []}

    notice_class = models.JSONField(default=classes_default_value, null=True)
    notice_townhouse = models.ForeignKey('clients.Client', null=True, related_name='notice_townhouse', on_delete=models.PROTECT)
    message = models.TextField(blank=True, null=True)
    media_url = models.TextField(blank=True, null=True)
    created = models.DateField(default=datetime.now, null=True)





class Enrollment(models.Model):
    student = models.ForeignKey('users.Student', null=True, related_name='student', on_delete=models.PROTECT)
    enrollment_class = models.ForeignKey('clients.Classes', null=True, related_name='enrollment_class', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)





class Unsubscribe(models.Model):
    enrollment_class = models.ForeignKey('clients.Classes', null=True, related_name='unsubscribe_class', on_delete=models.PROTECT)
    student = models.ForeignKey('users.Student', null=True, related_name='class_student', on_delete=models.PROTECT)
    teacher = models.ForeignKey('users.Teacher', null=True, related_name='class_teacher', on_delete=models.PROTECT)
    comment = models.TextField(null=True)
    created = models.DateField(default=datetime.now, null=True)





class Schedule(models.Model):
    student = models.ForeignKey('users.Student',null=True, related_name='student_schedule', on_delete=models.PROTECT)
    service = models.ForeignKey('clients.Service', null=True, related_name='service_schedule', on_delete=models.PROTECT)
    professional = models.ForeignKey('users.Teacher', null=True, related_name='professional_schedule', on_delete=models.PROTECT)
    date = models.DateField()
    hour = models.TimeField()
    status = models.BooleanField(default=False)
    created = models.DateField(default=datetime.now, null=True)



