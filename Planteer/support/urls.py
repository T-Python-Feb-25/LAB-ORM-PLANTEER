# contact/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.support, name='support'),
    path('contact/', views.contact_us, name='contact_us'),
    path('messages/', views.contact_messages, name='contact_messages'),
]