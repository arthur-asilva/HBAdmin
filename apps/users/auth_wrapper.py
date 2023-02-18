from rest_framework.response import Response
from django.shortcuts import redirect
from django.conf import settings
from apps.users.models import Token

def logged(function):
    
    def decorator(request, *args, **kwargs):
        if request.session.get('auth', None) is None:
            return redirect(settings.CURRENT_HOST)
        return function(request, *args, **kwargs)

    return decorator



def loggedToApi(function):

    def decorator(request, *args, **kwargs):
        user = Token.objects.filter(token=kwargs['token'])
        if user.exists():
            return function(request, *args, **kwargs)
        else:
            return Response({'erro': 'Acesso não autorizado.'})

    return decorator
