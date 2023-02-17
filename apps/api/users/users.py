from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from apps.users.models import Student, Teacher, Token, get_random_string
from apps.users.auth_wrapper import loggedToApi
import json


@api_view(['GET'])
@loggedToApi
def ApiGetStudent(request):
    serializer = UserSerializer(Student.objects.all(), many=True)
    return Response(serializer.data)





@api_view(['GET'])
def ApiGetStudents(request, id):
    serializer = UserSerializer(Student.objects.get(id=id))
    return Response(serializer.data)





@api_view(['POST'])
def ApiAuth(request):
    user = GetUserByGroup(request)
    token = get_random_string(8)

    if user.exists():
        if not Token.objects.filter(email=request.data['email']).exists():
            user = UserSerializer(user.first()).data
            Token.objects.create(email=request.data['email'], token=token)
            return Response({   'token': token   })
        else:
            Token.objects.filter()
            return Response({   'token': Token.objects.get(email=request.data['email']).token   })
    else:
        return Response({   'erro': 'Usuário não encontrado.'   })





def GetUserByGroup(request):
    params = { 'email': request.data['email'], 'password': request.data['password'], 'is_active': True }
    user_profile = { 'ALU': Student, 'PRO': Teacher }

    user = user_profile[request.data['access_group']].objects.filter(**params)

    return user