from django.urls import path
from .import views
app_name= 'plants'
urlpatterns = [
  path('new/', views.create_plants_view, name='create_plants_view'),
  path('all/', views.all_plants_view, name='all_plants_view'),
  path('detail/<plant_id>', views.plants_detail_view, name="plants_detail_view"), 
  path('update/<plant_id>', views.plants_update_view, name='plants_update_view'),
  path('delete/<plant_id>', views.plants_delete_view, name='plants_delete_view'),
  path('search/', views.search_plants_view, name='search_plants_view'),
  path('comment/add/<plant_id>', views.add_comment_view, name='add_comment_view')


]
