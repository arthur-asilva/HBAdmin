from django.urls import path
from .users import users
from .clients import clients

urlpatterns = [

    path('api/users/students/', users.ApiGetStudent),
    path('api/users/students/<int:id>/', users.ApiGetStudents),
    path('api/users/auth/', users.ApiAuth),

    path('api/users/teacher/<str:token>/classes/', clients.ApiGetClassesByTeacher),
    path('api/users/classes/<int:id>/', clients.ApiGetClassesByTownhouse)

]
