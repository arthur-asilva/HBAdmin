from django.shortcuts import redirect
from django.conf import settings

def logged(function):
    
    def decorator(request, *args, **kwargs):
        if request.session.get('auth', None) is None:
            return redirect(settings.CURRENT_HOST)
        return function(request, *args, **kwargs)

    return decorator