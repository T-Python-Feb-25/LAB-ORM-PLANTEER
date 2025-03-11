from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plants, Comment
from .forms import PlantsForm


def create_plants_view(request:HttpRequest):
  plant_form = PlantsForm()
  if request.method == 'POST':
    plant_form = PlantsForm(request.POST, request.FILES)
    if plant_form.is_valid():
      plant_form.save()
      #return redirect('main:home_view')
    else:
      return HttpResponse('Invalid form')
    
    
  return render(request, 'plants/create.html', {'plent_from':plant_form , 'CategoryChoices': reversed(Plants.CategoryChoices.choices)})


def all_plants_view(request:HttpRequest):
  plants = Plants.objects.all()
  return render(request, 'plants/all_plants.html', {'plants':plants})



def plants_detail_view(request:HttpRequest, plant_id:int):
  plant = Plants.objects.get(pk=plant_id)
  comments = Comment.objects.filter(plant=plant)

  related_plants = Plants.objects.filter(category=plant.category).exclude(id=plant_id).order_by('?')[:4]

  return render(request, 'plants/detail.html', {'plant':plant, 'comments':comments, 'related_plants' :related_plants})


def plants_update_view(request:HttpRequest, plant_id:int): 
  plant = Plants.objects.get(pk=plant_id)
  if request.method == 'POST':
    plant.name = request.POST['name']
    plant.about = request.POST['about']
    plant.used_for = request.POST['used_for']
    plant.category = request.POST['category']
    plant.is_edible = request.POST['is_edible']
    if 'image' in request.FILES:
      plant.image = request.FILES['image']
    plant.save()
    return redirect('plants:plants_detail_view', plant_id=plant.id)
  return render(request, 'plants/update.html', {'plant':plant})


def plants_delete_view(request:HttpRequest, plant_id:int):
  plant = Plants.objects.get(pk=plant_id)
  plant.delete()
  return redirect("main:home_view")



def filter_plants(request: HttpRequest, plant):
    if 'category' in request.GET and request.GET['category']:
        plant = plant.filter(category__iexact=request.GET['category'])

    is_edible_value = request.GET.get('is_edible')
    if is_edible_value == 'True':
        plant = plant.filter(is_edible=True)
    elif is_edible_value == 'False':
        plant = plant.filter(is_edible=False)

    return plant



def search_plants_view(request: HttpRequest):
    all_plants = Plants.objects.all()

    search_query = request.GET.get('Search', '')

    if search_query and len(search_query) >= 3:
        all_plants = all_plants.filter(name__icontains=search_query)
        print(all_plants)
   
    filtered_plants = filter_plants(request, all_plants) 

    if "order_by" in request.GET:
        if request.GET["order_by"] == "category":
            filtered_plants = filtered_plants.order_by("category")
        elif request.GET["order_by"] == "is_edible":
            filtered_plants = filtered_plants.order_by("-is_edible")

    return render(request, 'plants/search.html', {'filtered_plants': filtered_plants, 'search_query': search_query})



def add_comment_view(request:HttpRequest, plant_id):
   if request.method == 'POST':
      plant_object = Plants.objects.get(pk=plant_id)
      new_comment = Comment(plant=plant_object, full_name=request.POST['full_name'], content=request.POST['content'] )
      new_comment.save()
   return redirect('plants:plants_detail_view', plant_id=plant_id)