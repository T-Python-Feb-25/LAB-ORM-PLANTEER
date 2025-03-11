from django.urls import path
from . import views

urlpatterns = [
    path('plants/all/', views.all_plants, name='all_plants'),
    path('plants/<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('plants/new/', views.add_plant, name='add_plant'),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('plants/search/', views.search_plants, name='search_plants'),
]
