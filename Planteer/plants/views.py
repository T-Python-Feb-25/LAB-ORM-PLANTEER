from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Comment
from .forms import PlantForm, CommentForm
from django.http import JsonResponse

# Create your views here.


def all_plants(request):
    plants = Plant.objects.all().order_by('name')  # Order plants alphabetically by name
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=True)

    return render(request, 'plants/all_plants.html', {'plants': plants})


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)  # Get the plant instance
    related_plants = plant.related_plants.all()  # Get all related plants
    comments = plant.comments.all()  # Get all comments for the plant

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.plant = plant
            comment.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = CommentForm()

    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants,  # Pass related plants to the template
        'comments': comments,
        'form': form,
    })


def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plants:all_plants')
        else:
            print(form.errors)  # Debug form errors
    else:
        form = PlantForm()

    return render(request, 'plants/add_plant.html', {'form': form})


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)  # Get the plant instance
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)  # Bind the form to the plant instance
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)  # Pre-populate the form with the plant instance

    return render(request, 'plants/update_plant.html', {
        'plant': plant,
        'form': form,  # Pass the form to the template
    })

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    plant.delete()
    return redirect('plants:all_plants')


def search_plants(request):
    query = request.GET.get('q')
    plants = Plant.objects.filter(name__icontains=query) if query else []
    return render(request, 'plants/search_plants.html', {'plants': plants})

def get_plants_by_category(request):
    category = request.GET.get('category')
    plants = Plant.objects.filter(category=category).values('id', 'name')
    return JsonResponse({'plants': list(plants)})
