from django.shortcuts import render, redirect
from .models import Plant, Comment
from .forms import  PlantForm, CommentForm


def all_plants(request):
    plants = Plant.objects.all()
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)
     
    if is_edible == "true":
        plants = plants.filter(is_edible=True)
                 
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

    return render(request, 'all_plants.html', {'plants': plants})



def plant_detail(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    comments = Comment.objects.filter(plant=plant).order_by('-created_at')
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.plant = plant
            comment.save()
            return redirect('plant_detail', plant_id=plant.id)

    return render(request, 'plant_detail.html', {
        'plant': plant, 
        'related_plants': related_plants,
        'form': form,
        'comments': comments
    })


def search_plants(request):
    if "search" in request.GET:
        search_term = request.GET['search']
        plants = Plant.objects.filter(name__icontains=search_term)
    else:
        plants = Plant.objects.all()
    return render(request, 'plant_search.html', {'plants': plants})


def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()
    return render(request, 'plant_form.html', {'form': form})


def update_plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)  
    
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)  
    
    else:
        form = PlantForm(instance=plant)  
    
    return render(request, 'plant_update.html', {'form': form, 'plant': plant})



def delete_plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        plant.delete()
        return redirect('all_plants')
    return render(request, 'plant_delete.html', {'plant': plant})
