from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, StudentSerializer, AttendanceSerializer
from apps.api.clients.serializers import EnrollmentSerializer
from apps.users.models import Student, Teacher, Token, get_random_string, AttendenceList
from apps.clients.models import Enrollment, Classes
from apps.users.auth_wrapper import loggedToApi
from django.utils.timezone import now





@api_view(['POST'])
@loggedToApi
def ChangeAttendance(request, token, id):

    data = {
        'enrollments': [{'id': item.id, 'student_id': item.student.id, 'name': item.student.name}
                        for item in Enrollment.objects.filter(student__in=request.data['students'])],
        'attendence_class': Classes.objects.get(id=id),
        'date': request.data['date'],
        'details': request.data['details'],
        'photo': request.data['photo']
    }

    attendence = AttendenceList.objects.filter(date=request.data['date'], attendence_class__id=id)

    if attendence.count() == 0:
        AttendenceList.objects.create(**data)
    else:
        attendence.update(**data)

    return Response({'erro': False})





@api_view(['GET'])
@loggedToApi
def ApiLessonsList(request, token, id):
    user = Token.objects.get(token=token).email
    lessons = AttendanceSerializer(AttendenceList.objects.filter(attendence_class__id=id).order_by('-date'), many=True)
    return Response({'erro': False, 'lessons': lessons.data})





@api_view(['GET'])
@loggedToApi
def ApiLessonsLike(request, token, id):
    email = Token.objects.get(token=token).email
    user = Student.objects.get(email=email)
    lesson = AttendenceList.objects.get(id=id)
    if user.id not in lesson.likes['users']:
        lesson.likes['users'].append(user.id)
        lesson.total_likes = lesson.total_likes + 1
    else:
        lesson.likes['users'].remove(user.id)
        lesson.total_likes = lesson.total_likes - 1
    lesson.save()
    return Response({'erro': False, 'lesson': AttendanceSerializer(lesson).data})





@api_view(['POST'])
@loggedToApi
def GetAttendance(request, token):
    formated_date = datetime.strptime(request.data['date'], '%Y-%m-%d').date()
    attendence_list = AttendenceList.objects.filter(attendence_class_id=request.data['class_id'], date=formated_date)
    print(attendence_list)
    return Response({'erro': False, 'attendence_list': attendence_list.values()})





@api_view(['GET'])
@loggedToApi
def ApiGetStudent(request, token, id):
    serializer = StudentSerializer(Student.objects.get(id=id))
    score = 0
    frequency = AttendenceList.objects.values('enrollments').filter(date__year=now().year)
    full_list = []

    for x in frequency:
        full_list += x['enrollments']

    for x in full_list:
        if x['student_id'] == id:
            score += 1

    result = serializer.data.copy()
    result['score'] = score
    result['progress'] = round((score / frequency.count()), 1) * 100
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
    serializer = EnrollmentSerializer(Enrollment.objects.filter(enrollment_class__id=id).order_by('enrollment_class__weekday', 'enrollment_class__schedule', 'student__name'), many=True)
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





def ToPunchIn(request):
    # start = datetime.strptime(request.data['start'], '%Y-%m-%d').date()
    # end = datetime.strptime(request.data['end'], '%Y-%m-%d').date()
    # get_values = AttendenceList.objects.filter(enrollment_class__teacher__id=request.data['id']).values_list()
    return Response({'list': []})