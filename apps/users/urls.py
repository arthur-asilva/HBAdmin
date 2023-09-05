from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name="home_view"),
    path('dash/', views.DashView, name="dash_view"),
    path('logout/', views.LogoutView, name="logout_view"),
    path('password/', views.ChangePasswordView, name="changepassword_view"),
    path('teachers/', views.TeachersView, name="teachers_view"),
    path('students/', views.StudentsView, name="students_view"),
    path('administrators/', views.AdminstratorsView, name="administrators_view"),
]
