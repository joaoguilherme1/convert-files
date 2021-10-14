from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('converter', views.converter, name='converter'),
    path('heic_to_jpeg', views.heic_to_jpeg, name='heic_to_jpeg'),
]
