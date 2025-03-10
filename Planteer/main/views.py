from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Comment
# Create your views here.


# Home Page Page
def home_page_view(request :HttpRequest):
  plants = Plant.objects.all()[:3]
  return render(request, "main/index.html", {"plants":plants})
'''

    FLOWERING = "Flowering", "Flowering Plants"
    HERBS = "Herbs", "Herbs & Medicinal Plants"
    TREES = "Trees", "Trees & Shrubs"
    FRUIT = "Fruit", "Fruit Plants & Trees"
    VEGETABLES = "Vegetables", "Vegetable Plants"

'''
# All Plants Page
def all_plants_view(request :HttpRequest):
  choosen = ["FLOWERING", "HERBS", "TREES", "FRUIT", "VEGETABLES"]
  if "filter" in request.GET and request.GET["filter"] == "is_edible":
    plants = Plant.objects.filter(is_edible= 1)
    return render(request, "main/all_plants.html", {"plants":plants, "CategoryChoices": Plant.CategoryChoices.choices})
  elif "filter" in request.GET and request.GET["filter"].upper() in choosen:
      plants = Plant.objects.filter(category = request.GET["filter"])
      return render(request, "main/all_plants.html", {"plants":plants, "CategoryChoices": Plant.CategoryChoices.choices})


  plants = Plant.objects.all()
  return render(request, "main/all_plants.html", {"plants":plants, "CategoryChoices": Plant.CategoryChoices.choices})

# Plant Detail Page
def plant_detail_view(request :HttpRequest, plant_id):
  plant = Plant.objects.get(pk =plant_id)
  plants_related = Plant.objects.filter(category__contains = plant.category).exclude(id = plant_id)
  commnts = Comment.objects.filter(plant= plant_id)
  return render(request, "main/plant_detail.html", {"plant":plant, "plants_related": plants_related, "commnts":commnts})

# Search 

def plant_search_view(request: HttpRequest):
  if "search" in request.GET:
    plants = Plant.objects.filter(name__contains = request.GET['search'])
  return render(request, "main/search.html", {"plants": plants})

