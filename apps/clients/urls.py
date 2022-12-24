from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientsView, name='clients_view'),
]