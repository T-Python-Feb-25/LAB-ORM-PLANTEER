from django.urls import path
from . import views

app_name = "plant"

urlpatterns = [
    path("plants/new/" , views.add_plants , name="add_plants"),
    path("plants/<plant_id>/detail/" ,views.plant_detail , name="plant_detail" ),
    path("plants/all/",views.plant_view,name="plant_view"),
    path("plants/<plant_id>/update/",views.plant_update,name="plant_update"),
    path("plants/<plant_id>/delete/",views.plant_delete,name="plant_delete"),
    path("plants/<plant_id>/comment/",views.add_comment,name="add_comment"),
    path("plants/search/" , views.search_plant,name="search_plant")
]
