from django.shortcuts import render, redirect
from apps.users.auth_wrapper import logged
from .models import Service, Client, Classes, Enrollment
from apps.users.models import Teacher, Student

@logged
def ClientsView(request):

    edit_client = request.GET.get('c', False)
    client = None

    if edit_client:
        client = Client.objects.get(id=edit_client)

    if request.method == 'POST':
        
        if edit_client:
            Client.update(edit_client, request.POST.copy())
            return redirect('../clients')
        
        Client.create(request.POST.copy())
            

    data = {
        'services': Service.objects.all(),
        'clients': Client.objects.all(),
        'edit_client': edit_client,
        'client': client
    }

    return render(request, 'clients/clients.html', data)



@logged
def ClassesView(request):
    edit_class = request.GET.get('c', False)
    is_enrolling = request.POST.get('student_id', False) or request.GET.get('is_e', False)
    current_class = None
    enrollments_inclass = []

    if edit_class:
        current_class = Classes.objects.get(id=edit_class)
        enrollments_inclass = Enrollment.objects.values_list('student__id', flat=True).filter(enrollment_class__id=current_class.id)
        enrollments_inclass = list(enrollments_inclass)

    if request.method == 'POST':

        if edit_class and not is_enrolling:
            Classes.update(edit_class, request.POST.copy())
            return redirect('../clients/classes')

        if edit_class and is_enrolling:
            Enrollment.objects.create(
                student=Student.objects.get(id=is_enrolling),
                enrollment_class=Classes.objects.get(id=request.POST['class_id'])
            )
            return redirect(f"../clients/enrollments?c={edit_class}")

        Classes.create(request.POST.copy())

    data = {
        'classes': Classes.objects.all(),
        'teachers': Teacher.objects.filter(is_active=True),
        'clients': Client.objects.filter(is_active=True),
        'services': Service.objects.all(),
        'current_class': current_class,
        'edit_class': edit_class,
        'students': Student.objects.filter(is_active=True).exclude(id__in=enrollments_inclass),
        'is_enrolling': is_enrolling,
        'weekday_interval': range(0, 7)
    }
    
    return render(request, 'clients/classes.html', data)






@logged
def EnrollmentsView(request):

    current_class = request.GET.get('c', None)
    current_enroll = request.GET.get('e', None)

    if current_class is not None:
        current_class = Classes.objects.get(id=current_class)

    if current_enroll is not None:
        Enrollment.objects.filter(id=current_enroll).delete()
        return redirect(f"../clients/enrollments?c={current_class.id}")

    data = {
        'current_class': current_class,
        'enrollments': Enrollment.objects.filter(enrollment_class=current_class)
    }

    return render(request, 'clients/enrollments.html', data)