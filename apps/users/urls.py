from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name="home_view"),
    path('logout/', views.LogoutView, name="logout_view"),
    path('password/', views.ChangePasswordView, name="changepassword_view"),
    path('teachers/', views.TeachersView, name="teachers_view"),
    path('administrators/', views.AdminstratorsView, name="administrators_view"),
]
