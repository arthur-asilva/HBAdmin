from django.urls import path
from .users import users
from .clients import clients

urlpatterns = [

    path('api/users/auth/', users.ApiAuth),
    path('api/user/<str:token>/logout/', users.Logout),
    path('api/user/<str:token>/changepass/', users.ChangePassword),
    path('api/user/<str:token>/changephoto/', users.ChangePhoto),

    path('api/user/<str:token>/student/<int:id>/', users.ApiGetStudent),
    path('api/user/<str:token>/student/<int:id>/update/', users.ApiSetStudent),
    path('api/user/<str:token>/class/<int:id>/students/', users.ApiGetStudents),
    path('api/user/<str:token>/class/<int:id>/attendance/', users.ChangeAttendance),
    path('api/user/<str:token>/attendance/', users.GetAttendance),
    path('api/user/<str:token>/class/<int:id>/attendance_list/', users.ApiLessonsList),
    
    path('api/user/<str:token>/attendances/class/<int:id>/', users.ApiLessonsList),
    path('api/user/<str:token>/attendance_like/<int:id>/', users.ApiLessonsLike),
    path('api/user/<str:token>/subscribe/<int:id>/', users.ApiClassSubscribe),
    path('api/user/<str:token>/notices/<int:id>/', clients.ApiGetNotices),
    path('api/user/<str:token>/unsubscribe/<int:id>/', users.ApiClassUnsubscribe),
    path('api/user/<str:token>/schedule/', clients.ApiAddSchedule),
    path('api/user/<str:token>/schedules/', clients.ApiGetSchedules),
    path('api/user/<str:token>/schedule/change/<int:id>/', clients.ApiChangeSchedule),

    path('api/user/teacher/<str:token>/classes/', clients.ApiGetClassesByTeacher),
    path('api/user/<str:token>/client/<int:id>/', clients.ApiGetClassesByTownhouse)

]
