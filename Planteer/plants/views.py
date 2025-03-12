from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import plant

# Create your views here.
def all_plants(request:HttpRequest):
    #get all plants
    plants=plant.objects.all()
    return render(request, 'plants/all_plants.html',{"plant":plants})

def plants_detail(request:HttpRequest ,plant_id):
    plants=plant.objects.get(pk=plant_id)

    return render(request , 'plants/plants_detail.html', {"plant":plants})

def add_plants(request:HttpRequest):
    if request.method=="POST":
        new_plant=plant(name=request.POST["name"],about=request.POST["about"],used_for=request.POST["used_for"],
        image=request.FILES["image"],category=request.POST["category"],is_edible=request.POST["is_edible"],
        created_at=request.POST["created_at"])
        new_plant.save()
        return redirect('main:home')

    return render(request ,'plants/add_plants.html')

def update_plant(request:HttpRequest ,plant_id:int):
    plants=plant.objects.get(pk=plant_id)
    if request.method=="POST":
        plants.name=request.POST["name"]
        plants.about=request.POST["about"]
        plants.used_for=request.POST["used_for"]
        plants.category=request.POST["category"]
        plants.is_edible=request.POST["is_edible"]
        plants.created_at=request.POST["created_at"]
        if "image" in request.FILES:
            plants.image=request.FILES["image"]
        plants.save()
        return redirect('plants:plants_detail' ,plant_id=plants.id)
    return render(request ,'plants/update_plant.html',{"plant":plants})

def delete_plants(request:HttpRequest ,plant_id):
    plants=plant.objects.get(pk=plant_id)
    plants.delete()
    return redirect('main:home')
    return render(request , 'plants/delete_plants.html')

def search_plants(request:HttpRequest):
    return render(request , 'plants/search_plants.html')