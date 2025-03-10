from django.shortcuts import render
from django.http import HttpRequest
from plants.models import Plant

def home_view(requset:HttpRequest):

    plants=Plant.objects.all()[0:3]
    plants=Plant.objects.order_by("?")[:3]
    return render(requset,"main/home.html",{"plants":plants})
