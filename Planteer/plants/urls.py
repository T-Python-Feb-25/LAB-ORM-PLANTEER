from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("plants/new/", views.plants_create_view, name= "plants_create_view"),
]