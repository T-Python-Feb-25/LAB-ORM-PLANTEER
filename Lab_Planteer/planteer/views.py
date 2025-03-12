from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Plant
# Create your views here.

def add_plant_view(request: HttpRequest):
    
    return render(request,"planteer/add_plant.html")