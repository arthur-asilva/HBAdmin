from django.contrib import admin
from .models import Administrator, Teacher, Student, AttendenceList, Token

admin.site.register(Teacher)
admin.site.register(Administrator)
admin.site.register(Student)
admin.site.register(AttendenceList)
admin.site.register(Token)