from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest
from .forms import PlantForm
from .models import Plant,Comment



def add_plant_view(request: HttpRequest):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home_view')
    else:
        form = PlantForm()

    return render(request, 'plants/add_plant.html', {'form': form})

def all_plants_view(request:HttpRequest):
    categories = Plant.objects.values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category', '')
    
    if selected_category:
        plants = Plant.objects.filter(category=selected_category)
    else:
        plants = Plant.objects.all()
    context = {
        'plants': plants,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'plants/all_plants.html', context)

def plant_detail_view(request: HttpRequest, plant_id):
    plant_obj = Plant.objects.get(pk=plant_id)
    comments = []
    comments = Comment.objects.filter(plant=plant_obj)
    
    related_plants = Plant.objects.filter(category=plant_obj.category)[:3]
    return render(request, 'plants/plant_detail.html', {'plant': plant_obj, 'comments': comments,'related_plants':related_plants})

def plant_update_view(request: HttpRequest, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES,instance=plant)
        if form.is_valid():
            form.save()
            return redirect('main:home_view')
    else:
        form = PlantForm(request.POST, request.FILES,instance=plant)
    return render(request, 'plants/plant_update.html', {'plant': plant, 'form': form})


def plant_delete_view(request:HttpRequest,plant_id):
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect('main:home_view') 
 
def search_plant_view(request:HttpRequest):
    plants = []
    if 'search' in request.GET:
        plants = Plant.objects.filter(name__icontains = request.GET['name'])
    return render(request,'plants/search_plant.html',{'plants':plants})


def add_comment_view(request:HttpRequest,plant_id):
    if request.method == 'POST':
        plant_obj = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=plant_obj, name=request.POST['name'],comment=request.POST['comment'])
        new_comment.save()
    return redirect('plants:plant_detail_view',plant_id)
    
    