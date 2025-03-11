from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

from .forms import PlantForm
from .models import Plants ,Comment
# Create your views here.

def add_plants(request:HttpRequest):

    plant_form = PlantForm()

    if request.method == "POST":
        plant_form = PlantForm(request.POST,request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:home')

    return render(request,"plant/add_plant.html" , {"Plant_form" : PlantForm,"CategoryChoices" : Plants.CategoryChoices.choices })

def plant_detail(request:HttpRequest , plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    comment = Comment.objects.filter(plant=plant)
    return render(request,'plant/plant_detail.html',{"plant" : plant , "comment" : comment})

def plant_view(request: HttpRequest):
    plants = Plants.objects.all()
    
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    
    if category:
        plants = plants.filter(category=category)
    
    if is_edible and is_edible != '':
        is_edible = is_edible.lower() == 'true'
        plants = plants.filter(is_edible=is_edible)
    
    return render(request, "plant/plant_view.html", {"plant": plants,"categories": Plants.CategoryChoices.choices })

def plant_update(request:HttpRequest,plant_id:int):

    plant = Plants.objects.get(pk=plant_id)
    if request.method == "POST":
        
        plant_form = PlantForm(instance=plant, data=request.POST,files=request.FILES)
        plant_form.save()
        return redirect("plant:plant_detail", plant_id=plant.id)
    return render(request,"plant/plant_update.html", {"plant" : plant})

def plant_delete (request:HttpRequest , plant_id:int):
    plant = Plants.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:home")

def add_comment(request:HttpRequest, plant_id):

    if request.method == "POST":
        plant_object = Plants.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant_object,full_name=request.POST["full_name"],content=request.POST["content"])
        new_comment.save()

    return redirect("plant:plant_detail", plant_id=plant_id)

def search_plant(request:HttpRequest):
    if "search" in request.GET:
        plant = Plants.objects.filter(name__contains = request.GET['search'])
    return render(request, "plant/search.html" , {"plant" : plant})