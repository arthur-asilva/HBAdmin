from django.shortcuts import render
from .models import Administrator
from .auth_wrapper import logged
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
        else:
            print('user not found')

    return render(request, 'home.html')