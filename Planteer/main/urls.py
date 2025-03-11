from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/messages/', views.contact_messages, name='contact_messages'),
    path('contact/messages/<int:message_id>/', views.contact_message_detail, name='contact_message_detail'),

]

