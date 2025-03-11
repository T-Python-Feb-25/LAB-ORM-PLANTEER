from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path("contact/", views.contact_us_view, name="contact_us_view"),
    path("contact/messages/", views.contact_us_messages_view, name="contact_us_messages_view"),

]