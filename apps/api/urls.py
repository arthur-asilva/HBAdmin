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

    path('api/user/teacher/<str:token>/classes/', clients.ApiGetClassesByTeacher),
    path('api/user/<str:token>/client/<int:id>/', clients.ApiGetClassesByTownhouse)

]
