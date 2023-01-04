from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientsView, name='clients_view'),
    path('clients/classes', views.ClassesView, name='classes_view'),
    path('clients/enrollments', views.EnrollmentsView, name='enrollments_view'),
]