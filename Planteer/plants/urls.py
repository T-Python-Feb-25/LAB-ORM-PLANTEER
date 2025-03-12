from django.urls import path
from . import views

app_name="plants"

urlpatterns=[
    path("all/",views.all_plants, name="all_plants"),
    path("<int:plant_id>/detail/", views.plants_detail , name="plants_detail"),
    path("new/", views.add_plants ,name="add_plants"),
    path("<int:plant_id>/update/" ,views.update_plant , name="update_plant"),
    path("<int:plant_id>/delete/" ,views.delete_plants , name="delete_plants"),
    path("search/" , views.search_plants ,name="search_plants"),
]