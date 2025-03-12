from django.urls import path
from . import views
app_name = "app_planteer"
urlpatterns = [
    path("", views.home_page, name="home_page"),
    path('plants/all/', views.all_plants, name='all_plants'),
    path('plants/<plant_id>/detail/', views.plant_detail, name='plant_detail'),

    path('plants/<int:plant_id>/edit/', views.plant_edit, name='plant_edit'),  
    path('plants/<int:plant_id>/delete/', views.plant_delete, name='plant_delete'),  


    path('plants/new/', views.add_plant, name='add_plant'),
    path('plants/search/', views.search_plants, name='search_plants'),

    path('contact/', views.contact, name='contact'),
     path('contact/messages/', views.contact_page_messages, name='contact_page_messages'),
]
