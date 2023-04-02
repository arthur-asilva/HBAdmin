from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, StudentSerializer
from apps.api.clients.serializers import EnrollmentSerializer
from apps.users.models import Student, Teacher, Token, get_random_string, AttendenceList
from apps.clients.models import Enrollment
from apps.users.auth_wrapper import loggedToApi
from django.utils.timezone import now




@api_view(['POST'])
@loggedToApi
def ChangeAttendance(request, token, id):

    enrollments = Enrollment.objects.filter(enrollment_class=id, student__in=request.data['students'])
    attendence_list = [AttendenceList(**{'enrollment': x, 'date': request.data['date'], 'status': request.data['status']}) for x in enrollments]
    
    try:
        AttendenceList.objects.filter(enrollment__enrollment_class__id=id, date=request.data['date']).delete()
    finally:
        AttendenceList.objects.bulk_create(attendence_list)

    return Response({'erro': False})





@api_view(['GET'])
@loggedToApi
def ApiGetStudent(request, token, id):
    serializer = StudentSerializer(Student.objects.get(id=id))
    score = AttendenceList.objects.filter(enrollment__student__id=id, date__year=now().year).count()
    result = serializer.data.copy()
    result['score'] = score
    return Response(result)





@api_view(['POST'])
@loggedToApi
def ApiSetStudent(request, token, id):
    
    Student.objects.filter(id=id).update(**request.data)
    student = StudentSerializer(Student.objects.get(id=id))
    return Response(student.data)





@api_view(['POST'])
@loggedToApi
def ChangePassword(request, token):
    user_profile = { 'ALU': Student, 'PRO': Teacher }
    user = user_profile[request.data['access_group']].objects.get(email=request.data['email'])
    user.password = request.data['new_password']
    user.save()
    return Response({ 'erro': False, 'message': 'Operação concluída com sucesso.' })




@api_view(['GET'])
@loggedToApi
def Logout(request, token):
    Token.objects.get(token=token).delete()
    return Response({ 'erro': False, 'message': 'Operação concluída com sucesso.' })




@api_view(['POST'])
@loggedToApi
def ChangePhoto(request, token):
    user_profile = { 'ALU': Student, 'PRO': Teacher }
    user = user_profile[request.data['access_group']].objects.get(email=request.data['email'])
    user.photo = request.data['photo']
    user.save()
    return Response({ 'erro': False, 'message': 'Operação concluída com sucesso.', 'photo': request.data['photo'] })





@api_view(['GET'])
@loggedToApi
def ApiGetStudents(request, token, id):
    serializer = EnrollmentSerializer(Enrollment.objects.filter(enrollment_class__id=id).order_by('enrollment_class__weekday', 'enrollment_class__schedule'), many=True)
    return Response(serializer.data)





@api_view(['POST'])
def ApiAuth(request):
    user = GetUserByGroup(request)

    if user.exists():
        user = UserSerializer(user.first()).data
        
        if not Token.objects.filter(email=request.data['email']).exists():
            Token.objects.create(email=request.data['email'], token=get_random_string(8))

        return Response({   'user': user, 'token': Token.objects.get(email=request.data['email']).token   })
    else:
        return Response({   'erro': 'Usuário não encontrado.'   })





def GetUserByGroup(request):
    params = { 'email': request.data['email'], 'password': request.data['password'], 'is_active': True }
    user_profile = { 'ALU': Student, 'PRO': Teacher }

    user = user_profile[request.data['access_group']].objects.filter(**params)

    return user