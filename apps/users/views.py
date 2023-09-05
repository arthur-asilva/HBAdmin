from django.shortcuts import render, redirect
from .models import Administrator, Teacher, Student
from .auth_wrapper import logged
from apps.clients.models import Service
from django.conf import settings
import json


def HomeView(request):

    if request.method == 'POST':

        user_data = {
            'email': request.POST['user'],
            'password': request.POST['pass'],
            'is_active': True,
            'access_group': 'ADM'
        }

        user = Administrator.objects.filter(**user_data).values('id', 'name', 'email', 'photo', 'access_group')
        
        if user.exists():
            request.session['auth'] = json.dumps(user.first())
            return redirect('../clients/')
        else:
            print('user not found')

    return render(request, 'home.html')

@logged
def LogoutView(request):
    is_logged = request.session.get('auth', None)
    if is_logged is not None:
        request.session.pop('auth')
    return redirect('../')


@logged
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
        'edit_teacher': edit_teacher,
        'weekday_interval': range(0, 7)
    }

    if request.method == 'POST':
        request_data = request.POST.copy()
        if edit_teacher:
            Teacher.update(teacher.id, request_data)
            return redirect('../teachers/')
        else:
            Teacher.create(request_data)

    return render(request, 'users/teachers.html', data)


@logged
def AdminstratorsView(request):

    admin = request.GET.get('u', None)
    edit_admin = False

    if admin is not None:
        admin = Administrator.objects.get(id=admin)
        edit_admin = True

    data = {
        'administrators': Administrator.objects.all(),
        'services': Service.objects.all(),
        'administrator': admin,
        'edit_admin': edit_admin
    }

    if request.method == 'POST':
        request_data = request.POST.copy()
        if edit_admin:
            Administrator.update(admin.id, request_data)
            return redirect('../administrators/')
        else:
            Administrator.create(request_data)

    return render(request, 'users/administrators.html', data)




@logged
def ChangePasswordView(request):

    if request.method == 'POST':
        
        current_user = json.loads(request.session['auth'])
        current_user = Administrator.objects.get(id=current_user['id'])
        
        if current_user.password == request.POST['current_pass']:
            current_user.password = request.POST['new_pass']
            current_user.save()
            return redirect(settings.CURRENT_HOST)
        

    return render(request, 'users/change_password.html')




@logged
def StudentsView(request):

    student = request.GET.get('s', None)
    edit_student = False

    if student is not None:
        student = Student.objects.get(id=student)
        edit_student = True

    data = {
        'students': Student.objects.all(),
        'student': student,
        'edit_student': edit_student
    }

    if request.method == 'POST':
        request_data = request.POST.copy()
        if edit_student:
            Student.update(student.id, request_data)
            return redirect('../students/')
        else:
            Student.create(request_data)

    return render(request, 'users/students.html', data)




@logged
def DashView(request):
    return render(request, 'dash.html')