def logged(function):
    
    def decorator(request, *args, **kwargs):
        print(request)
        return function(request, *args, **kwargs)

    return decorator