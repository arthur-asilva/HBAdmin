from django.contrib import admin
from .models import Administrator, Teacher, Student, Enrollment, AttendenceList

admin.site.register(Teacher)
admin.site.register(Administrator)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(AttendenceList)
