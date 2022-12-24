from django.shortcuts import render, redirect
from .models import Service, Client

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
