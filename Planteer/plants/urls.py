from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path("plants/new/", views.create_plants_view, name="create_plants_view"),
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("plants/<plant_id>/detail/", views.plant_detail_view, name="plant_detail_view"),
    path("plants/<plant_id>/update/", views.plant_update_view, name="plant_update_view"),
    path("plants/<plant_id>/delete/", views.plant_delete_view, name="plant_delete_view"),
    path("plants/search/", views.plant_search_view, name="plant_search_view"),
    path("plants/comment/<plant_id>", views.add_comment_view, name="add_comment_view"),

]
