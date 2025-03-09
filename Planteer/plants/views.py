from django.shortcuts import render,redirect
from .models import Plant
# Create your views here.
from django.http import HttpRequest, HttpResponse
# Create your views here.
def all_plants_view(request : HttpRequest):
	plants = Plant.objects.all()
	return render(request,'plants/all_plants.html',{"plants": plants})

def create_plants_view(request : HttpRequest):
	if request.method == "POST":
		new_plant=Plant(name=request.POST['name'],about=request.POST['about'],used_for=request.POST['used_for'],category=request.POST['category'],is_edible=request.POST['is_edible'],image=request.FILES['image'])
		new_plant.save()
		return redirect('plants:all_plants_view')
	return render(request,'plants/create_plant.html')



def plant_detail_view(request: HttpRequest, plant_id:int):
	plants = Plant.objects.get(pk=plant_id)
	return render(request, "plants/plant_detail.html", {"plants": plants})


def plant_update_view(request: HttpRequest, plant_id:int):
	plants = Plant.objects.get(pk=plant_id)
	if request.method == "POST":
		plants.name = request.POST['name']
		plants.about = request.POST['about']
		plants.used_for = request.POST['used_for']
		plants.category = request.POST['category']
		plants.is_edible = request.POST['is_edible']
		if 'image' in request.FILES:
			plants.image = request.FILES['image']
		plants.save()
		return redirect('plants:plant_detail_view', plant_id)
	return render(request, "plants/plant_update.html", {"plants": plants})



def plant_delete_view(request: HttpRequest, plant_id: int):
    plants = Plant.objects.get(pk=plant_id)
    plants.delete()
    return redirect('plants:all_plants_view')


