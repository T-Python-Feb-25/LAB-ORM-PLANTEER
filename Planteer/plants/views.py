
# Create your views here.
from django.shortcuts import render
from .models import Plant



def all_plants(request):
    category = request.GET.get('category', None)
    is_edible = request.GET.get('is_edible', None)

    plants = Plant.objects.all()

    if category:
        plants = plants.filter(category=category)
    if is_edible is not None:
        plants = plants.filter(is_edible=True)

    return render(request, 'plants/all_plants.html', {'plants': plants})




from django.shortcuts import render, get_object_or_404
from .models import Plant, Comment

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)
    comments = plant.comments.all()

    return render(request, 'plants/plant_detail.html', {'plant': plant, 'related_plants': related_plants, 'comments': comments})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Comment

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    comments = Comment.objects.filter(plant=plant)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        content = request.POST.get("content")
        Comment.objects.create(plant=plant, full_name=full_name, content=content)
        return redirect('plant_detail', plant_id=plant.id)  
    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants,
        'comments': comments
    })








from django.shortcuts import render
from .models import Plant

def search_plants(request):
    query = request.GET.get('q', '') 
    results = Plant.objects.filter(name__icontains=query) if query else []
    
    return render(request, 'plants/search_results.html', {'query': query, 'results': results})









from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm  
from django.contrib import messages

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Plant added successfully!")
            return redirect('all_plants')  
    else:
        form = PlantForm()
    
    return render(request, 'plants/add_plant.html', {'form': form})






from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from .forms import PlantForm

def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/update_plant.html', {'form': form, 'plant': plant})








def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == "POST":
        plant.delete()
        return redirect('all_plants')

    return render(request, 'plants/delete_plant.html', {'plant': plant})










from django.shortcuts import render, get_object_or_404
from .models import Plant, Comment

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:3]
    comments = Comment.objects.filter(plant=plant)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        content = request.POST.get("content")
        Comment.objects.create(plant=plant, full_name=full_name, content=content)

    return render(request, "plants/plant_detail.html", {
        "plant": plant,
        "related_plants": related_plants,
        "comments": comments,
    })




from django.shortcuts import render
from .models import Plant
import random

def home(request):
    all_plants = list(Plant.objects.all())
    featured_plants = random.sample(all_plants, min(len(all_plants), 3))
    return render(request, 'home.html', {'featured_plants': featured_plants})
