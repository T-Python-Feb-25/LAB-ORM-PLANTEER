
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plant, Category

def home_view(request):
    plants = Plant.objects.all()
    return render(request, 'app_main/home.html', {'plants': plants})

def plant_view(request: HttpRequest):
    plants = Plant.objects.all()  
    return render(request, "app_main/all_plant.html", {'plants': plants})  

def detail_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)  
    return render(request, "app_main/detail.html", {'plant': plant})

def plants_new_view(request: HttpRequest):
    if request.method == 'POST':
        new_plant = Plant(
            name=request.POST.get('name'),  
            about=request.POST.get('about'),
            used_for=request.POST.get('used_for'),  
            image=request.FILES.get('image'),  
            categoy=request.POST.get('categoy'),  
            is_edible='is_edible' in request.POST  
        )
        new_plant.save()
        return redirect('app_main:home_view')  
    
    return render(request, "app_main/new_plants.html")

def update_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)  

    if request.method == 'POST':
        plant.name = request.POST.get('name')  
        plant.about = request.POST.get('about')
        plant.used_for = request.POST.get('used_for')
        plant.categoy = request.POST.get('categoy')
        plant.is_edible = 'is_edible' in request.POST  
        
        if 'image' in request.FILES:
            plant.image = request.FILES['image']
        
        plant.save()  
        return redirect('app_main:home_view')

    return render(request, "app_main/update.html", {'plant': plant})

def delete_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)
    plant.delete()
    return redirect('app_main:home_view')  

def search_view(request: HttpRequest):
    query = request.GET.get('q', '').strip() 
    plants = Plant.objects.filter(name__icontains=query) if query else []  
    categories = Category.objects.all()

    return render(request, 'app_main/search.html', {
        'plants': plants, 
        'categories': categories, 
        'query': query
    })
