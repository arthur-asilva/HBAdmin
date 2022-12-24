from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    services = models.JSONField(default={})
