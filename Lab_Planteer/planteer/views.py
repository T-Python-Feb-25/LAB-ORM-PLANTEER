from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
# Create your views here.

def add_plant_view(request: HttpRequest):
    if request.method=="POST":
        new_plant=Plant(title=request.POST["title"], content=request.POST["content"], published_at=request.POST["published_at"], plant_image=request.FILES["plant_image"] )
        new_plant.save()
        
        return redirect('main:all_plant_view')
    
    
    return render(request,"planteer/add_plant.html")

def plant_detail_view(request: HttpRequest , plant_id:int):
    
    plant=Plant.objects.get(pk=plant_id)
    
    return render(request,"planteer/plant_detail.html",{"plant":plant})


def plant_update_view(request: HttpRequest , plant_id:int):
    
    plant=Plant.objects.get(pk=plant_id)
    
    if request.method=="POST":
        plant.title=request.POST["title"] 
        plant.content=request.POST["content"] 
        plant.published_at=request.POST["published_at"] 
        if "plant_image" in request.FILES: plant.plant_image=request.FILES["plant_image"] 
        plant.save()
        
        return redirect('planteer:plant_detail_view',plant_id=plant.id)
    
    return render(request,"planteer/plant_update.html",{"plant":plant})


def plant_delete_view(request: HttpRequest , plant_id:int):
    
    plant=Plant.objects.get(pk=plant_id)
    plant.delete()
    
    return redirect('main:all_plant_view')
