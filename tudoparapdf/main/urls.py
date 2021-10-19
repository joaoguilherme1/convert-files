from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf', views.pdf, name='pdf'),
    path('csv', views.csv, name='csv'),
    path('docx', views.docx, name='docx'),
    path('heic_to_jpeg', views.heic_to_jpeg, name='heic_to_jpeg'),
]
