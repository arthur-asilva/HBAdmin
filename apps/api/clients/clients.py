from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ClassSerializer
from apps.clients.models import Classes
from apps.users.models import Token
from apps.users.auth_wrapper import loggedToApi



@api_view(['GET'])
@loggedToApi
def ApiGetClassesByTeacher(request, token):
    teacher = Token.objects.get(token=token)
    serializer = ClassSerializer(Classes.objects.filter(teacher__email=teacher.email), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@loggedToApi
def ApiGetClassesByTownhouse(request, token, id):
    serializer = ClassSerializer(Classes.objects.filter(client__id=id), many=True)
    return Response(serializer.data)