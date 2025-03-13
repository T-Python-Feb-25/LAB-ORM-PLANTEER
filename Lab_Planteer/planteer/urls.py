from django.urls import path
from . import views

app_name="planteer"

urlpatterns = [
    
    path("add/plant/", views.add_plant_view,name="add_plant_view"),
    
    path("detail/<plant_id>",views.plant_detail_view,name="plant_detail_view"),
    
    path("update/<plant_id>",views.plant_update_view,name="plant_update_view"),
    
    path("delete/<plant_id>",views.plant_delete_view,name="plant_delete_view")

]