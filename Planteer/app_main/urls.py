from django.urls import path
from . import views

app_name= 'app_main'


urlpatterns = [
path("", views.home_view, name="home_view"),
path("plants/all/", views.plant_view, name="plant_view"),
path("plants/<plant_id>/detail/", views.detail_view, name="detail_view"),
path("plants/new/", views.plants_new_view, name="plants_new_view"),
path("plants/<plant_id>/update/", views.update_view, name="update_view"),
path("plants/<plant_id>/delete/", views.delete_view, name="delete_view"),
path("plants/search/", views.search_view, name="search_view"),
]
