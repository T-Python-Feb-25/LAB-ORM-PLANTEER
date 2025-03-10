from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Comment
from .forms import CommentForm, PlantForm


def all_plants(request):
    category = request.GET.get('category', '')
    is_edible = request.GET.get('is_edible', '')

    plants = Plant.objects.all()

    if category:
        plants = plants.filter(category=category)
    if is_edible == 'true':
        plants = plants.filter(is_edible=True)
    elif is_edible == 'false':
        plants = plants.filter(is_edible=False)

    categories = dict(Plant.CATEGORY_CHOICES)

    return render(request, 'plants/all_plants.html', {
        'plants': plants,
        'categories': categories
    })


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]  
    comments = plant.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.plant = plant
            comment.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = CommentForm()

    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants,
        'comments': comments,
        'form': form
    })


def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()

    return render(request, 'plants/add_plant.html', {'form': form})


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/update_plant.html', {'form': form, 'plant': plant})


def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == "POST":
        plant.delete()
        return redirect('all_plants')  

    return render(request, 'plants/delete_plant.html', {'plant': plant})

def search_plants(request):
    query = request.GET.get('q', '')
    plants = Plant.objects.filter(name__icontains=query) if query else []

    return render(request, 'plants/search.html', {'plants': plants, 'query': query})
