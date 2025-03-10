from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("plants/new/", views.plants_create_view, name= "plants_create_view"),
    path("plants/<plant_id>/update/", views.plants_update_view, name= "plants_update_view"),
    path("plants/<plant_id>/delete/", views.plants_delete_view, name= "plants_delete_view"),
    path("commnt/new/<plant_id>", views.commnt_create_view, name= "commnt_create_view"),
]