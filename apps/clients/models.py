from django.db import models



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
    

    def __str__(self):
        return self.name
