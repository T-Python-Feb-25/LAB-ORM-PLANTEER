from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    
    path("", views.Home_view,name="Home_view"),
    path("all/plant", views.all_plant_view,name="all_plant_view"),

]