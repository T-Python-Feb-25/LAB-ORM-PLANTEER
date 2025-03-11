from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant, Comment
 # Create your views here.

def home_page (request : HttpRequest):
  
    return render(request, 'app_planteer/home_page.html')

def all_plants(request : HttpRequest):

    planteer =Plant.objects.all()
    return render(request, 'app_planteer/all_plants.html',{"planteer":planteer})

def add_plant(request : HttpRequest):

    if request.method=="POST":
       new_plant=Plant(name=request.POST["name"],description=request.POST["description"])
       new_plant.save()
    #print(request.POST)
   
    return render(request, 'app_planteer/add_plant.html')

def search_plants(request : HttpRequest):
    return render(request, 'app_planteer/search_plants.html')

def contact(request : HttpRequest):
    return render(request, 'app_planteer/contact.html')

def plant_detail(request : HttpRequest , plant_id):
    return render(request, 'app_planteer/plant_detail.html')

