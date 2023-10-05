from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ClassSerializer, SchedulesSerializer, ServicesSerializer
from apps.clients.models import Classes, Schedule, Service
from apps.users.models import Token, Student, Teacher
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




@api_view(['POST'])
@loggedToApi
def ApiAddSchedule(request, token):
    data = {
        'student': Student.objects.get(id=request.data['student']),
        'service': Service.objects.get(id=request.data['service']),
        'date': request.data['date'],
        'hour': request.data['hour']
    }
    Schedule.objects.create(**data)
    return Response({'error': False})



@api_view(['GET'])
@loggedToApi
def ApiGetSchedules(request, token):
    schedules = Schedule.objects.all().order_by('-date', '-hour')
    services = Service.objects.all().order_by('-name')

    data = {
        'error': False, 
        'data': SchedulesSerializer(schedules, many=True).data, 
        'count': schedules.count(), 
        'services': ServicesSerializer(services, many=True).data
    }

    return Response(data)



@api_view(['POST'])
@loggedToApi
def ApiChangeSchedule(request, token, id):
    professional = Teacher.objects.get(id=request.data['professional'])
    Schedule.objects.filter(id=id).update(professional=professional, status=request.data['status'])
    schedules = Schedule.objects.all().order_by('-date', '-hour')
    return Response({'error': False, 'data': SchedulesSerializer(schedules, many=True).data, 'count': schedules.count()})