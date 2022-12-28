from django.shortcuts import render, redirect
from apps.users.auth_wrapper import logged
from .models import Service, Client, Classes
from apps.users.models import Teacher

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
    current_class = None

    if edit_class:
        current_class = Classes.objects.get(id=edit_class)

    if request.method == 'POST':
        if edit_class:
            Classes.update(edit_class, request.POST.copy())
            return redirect('../clients/classes')

        Classes.create(request.POST.copy())

    data = {
        'classes': Classes.objects.all(),
        'teachers': Teacher.objects.filter(is_active=True),
        'clients': Client.objects.filter(is_active=True),
        'services': Service.objects.all(),
        'current_class': current_class,
        'edit_class': edit_class,
        'weekday_interval': range(0, 7)
    }

    return render(request, 'clients/classes.html', data)
