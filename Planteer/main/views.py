from django.shortcuts import get_object_or_404, redirect, render
from .models import Plant
from .forms import PlantForm

# Home Page
def home(request):
    plants = Plant.objects.all()  # Query to get all plants
    return render(request, 'html/home.html', {'plants': plants})

# All Plants page
def all_plants(request):
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=is_edible)

    categories = Plant.objects.values_list('category', flat=True).distinct()

    return render(request, 'html/all_plants.html', {
        'plants': plants,
        'categories': categories,
        'selected_category': category,
        'selected_is_edible': is_edible,
    })

def search_plants(request):
    query = request.POST.get('search')
    if query:
        plants = Plant.objects.filter(name__icontains=query)
    else:
        plants = Plant.objects.all()
    return render(request, 'html/search_plants.html', {'plants': plants, 'query': query})

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'some_view_name' with the name of the view to redirect to
    else:
        form = PlantForm()
    return render(request, 'html/add_plant.html', {'form': form})

# Update Plant Page
def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('all_plants')  # Redirect to the correct URL pattern
    else:
        form = PlantForm(instance=plant)
    return render(request, 'html/update_plant.html', {'form': form})

# Delete Plant Page
def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('all_plants')  # Ensure this line redirects to the correct URL pattern
    return render(request, 'html/delete_plant.html', {'plant': plant})


# Plant Detail Page
def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:3]  # Get related plants by category
    return render(request, 'html/plant_detail.html', {'plant': plant, 'related_plants': related_plants})