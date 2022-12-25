from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name="home_view"),
    path('teachers/', views.TeachersView, name="teachers_view"),
]
