from django.urls import path
from .views import all_plants, plant_detail, search_plants ,add_plant, update_plant

urlpatterns = [
    path('all/', all_plants, name='all_plants'),
    path('<int:plant_id>/detail/', plant_detail, name='plant_detail'),
    path('search/', search_plants, name='search_plants'), 
    path('new/', add_plant, name='add_plant'), 
    path('plants/<int:plant_id>/update/', update_plant, name='update_plant'),


]


from .views import delete_plant

urlpatterns += [
    path('plants/<int:plant_id>/delete/', delete_plant, name='delete_plant'),
]
