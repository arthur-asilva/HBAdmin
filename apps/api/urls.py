from django.urls import path
from .users import users
from .clients import clients

urlpatterns = [

    path('api/users/auth/', users.ApiAuth),
    path('api/users/students/', users.ApiGetStudent),

    path('api/user/<str:token>/class/<int:id>/students/', users.ApiGetStudents),

    path('api/user/teacher/<str:token>/classes/', clients.ApiGetClassesByTeacher),
    path('api/user/<str:token>/client/<int:id>/', clients.ApiGetClassesByTownhouse)

]
