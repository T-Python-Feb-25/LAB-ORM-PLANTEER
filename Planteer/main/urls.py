from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('/', views.home, name='home'),
    path('plants/all/', views.plant, name= 'plant'),
    path('plants/<plant_id>/detail/', views.detail, name='detail'),
    path('plants/new/', views.add, name='add'),
    path('plants/<plant_id>/update/', views.update, name='update'),
    path('plants/<plant_id>/delete/', views.delete, name='delete'),
    path('plants/search/', views.search, name='search'),

]