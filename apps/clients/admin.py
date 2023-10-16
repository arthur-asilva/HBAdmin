from django.contrib import admin
from .models import Service, Client, Classes, Enrollment, Schedule, Unsubscribe, Notice





admin.site.register(Notice)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Classes)
admin.site.register(Enrollment)
admin.site.register(Schedule)
admin.site.register(Unsubscribe)
