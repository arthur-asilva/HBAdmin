from django.shortcuts import render

def ClientsView(request):

    data = {
        'services': range(0, 15)
    }

    return render(request, 'clients/clients.html', data)
