from django.urls import path
from . import views

urlpatterns = [
    path('qrcode', views.GenereteQRView, name="qrcode_view")
]