from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('all/', views.all_plants, name='all_plants'),
    path('<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('new/', views.add_plant, name='add_plant'),
    path('<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('search/', views.search_plants, name='search_plants'),
    path('get_plants_by_category/', views.get_plants_by_category, name='get_plants_by_category'),  # Add this line
]
