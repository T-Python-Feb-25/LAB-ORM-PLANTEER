from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from planteer.models import Plant
# Create your views here.


def Home_view(request: HttpRequest):
    plants=Plant.objects.all()
    return render(request, "main/index.html", {"plants":plants})

def all_plant_view(request: HttpRequest):
    plants=Plant.objects.all()
    
    return render(request, "main/all_plant.html", {"plants":plants})