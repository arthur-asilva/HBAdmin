from django.shortcuts import render, redirect
from .models import Administrator, Teacher
from .auth_wrapper import logged
from apps.clients.models import Service
import json


def HomeView(request):

    if request.method == 'POST':

        user_data = {
            'email': request.POST['user'],
            'password': request.POST['pass'],
            'is_active': True,
            'access_group': 'ADM'
        }

        user = Administrator.objects.filter(**user_data).values('id', 'name', 'email', 'photo')
        
        if user.exists():
            request.session['auth'] = json.dumps(user.first())
            return redirect('../clients/')
        else:
            print('user not found')

    return render(request, 'home.html')



def TeachersView(request):

    teacher = request.GET.get('t', None)
    edit_teacher = False

    if teacher is not None:
        teacher = Teacher.objects.get(id=teacher)
        edit_teacher = True


    data = {
        'teachers': Teacher.objects.all(),
        'services': Service.objects.all(),
        'teacher': teacher,
        'edit_teacher': edit_teacher
    }

    if request.method == 'POST':
        request_data = request.POST.copy()
        if edit_teacher:
            Teacher.update(teacher.id, request_data)
            return redirect('../teachers/')
        else:
            Teacher.create(request_data)

    return render(request, 'users/teachers.html', data)