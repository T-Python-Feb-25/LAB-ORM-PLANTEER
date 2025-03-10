from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path("", views.home_page_view, name= "home_page_view"),
  path("plants/all/", views.all_plants_view, name= "all_plants_view"),
  path("plants/<plant_id>/detail/", views.plant_detail_view, name= "plant_detail_view"),
  path("plants/search/", views.plant_search_view, name= "plant_search_view"),
]