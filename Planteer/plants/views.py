from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Plant, Comment
# Create your views here.


# Create Plants
def plants_create_view(request: HttpRequest):
  if request.method == "POST":
    new_plant = Plant(name= request.POST['name'], about= request.POST['about'], user_for= request.POST['user_for'], category = request.POST['category'], is_edible= request.POST['is_edible'], image= request.FILES['image'])
    new_plant.save()
    return redirect("main:home_page_view")
  return render(request, "plants/create_plant.html", {"CategoryChoices": Plant.CategoryChoices.choices})

# Update View
def plants_update_view(request: HttpRequest, plant_id):
  if request.method == "POST":
    plant = Plant.objects.get(pk= plant_id)
    plant.name = request.POST["name"]
    plant.about = request.POST["about"]
    plant.user_for = request.POST["user_for"]
    plant.category = request.POST["category"]
    plant.is_edible = request.POST["is_edible"]
    plant.save()
    return redirect("main:home_page_view")
  old_plant = Plant.objects.get(pk= plant_id)
  return render(request, "plants/update.html", {"old_plant":old_plant, "CategoryChoices" : Plant.CategoryChoices.choices})

# Delete View
def plants_delete_view(request: HttpRequest, plant_id):
  plant_del = Plant.objects.get(pk= plant_id)
  plant_del.delete()
  return redirect("main:home_page_view")

# Add Commnt

def commnt_create_view(request: HttpRequest, plant_id):
  if request.method == "POST":
    plant_obj = Plant.objects.get(pk=plant_id)
    new_commnt = Comment(plant = plant_obj, full_name= request.POST['full_name'], content= request.POST['content'])
    new_commnt.save()
    return redirect("main:plant_detail_view", plant_id)