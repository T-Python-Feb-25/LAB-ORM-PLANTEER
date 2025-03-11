from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/all/', views.all_plants, name='all_plants'),
    path('plants/<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('search/', views.search_plants, name='search_plants'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
