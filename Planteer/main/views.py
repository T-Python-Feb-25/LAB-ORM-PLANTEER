from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
# Create your views here.


# Home Page Page
def home_page_view(request :HttpRequest):
  plants = Plant.objects.all()[:3]
  return render(request, "main/index.html", {"plants":plants})

# All Plants Page
def all_plants_view(request :HttpRequest):
  if "filter" in request.GET and request.GET["filter"] == "is_edible":
    plants = Plant.objects.filter(is_edible= 1)
    return render(request, "main/all_plants.html", {"plants":plants})


  plants = Plant.objects.all()
  return render(request, "main/all_plants.html", {"plants":plants})

# Plant Detail Page
def plant_detail_view(request :HttpRequest, plant_id):
  plant = Plant.objects.get(pk =plant_id)
  plants_related = Plant.objects.filter(category__contains = plant.category).exclude(id = plant_id)
  return render(request, "main/plant_detail.html", {"plant":plant, "plants_related": plants_related})



