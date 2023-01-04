from django.contrib import admin
from .models import Service, Client, Classes, Enrollment

admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Classes)
admin.site.register(Enrollment)
