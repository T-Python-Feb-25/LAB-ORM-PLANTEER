from django.urls import path
from . import views 

app_name = "contact"

urlpatterns = [
  path("contact/", views.contact_page_view , name= "contact_page_view"),
  path("contact/messages/", views.contact_messages_page_view , name= "contact_messages_page_view"),
]