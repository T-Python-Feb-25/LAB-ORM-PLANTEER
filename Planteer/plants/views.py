from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Plant
# Create your views here.


# Create Plants
def plants_create_view(request: HttpRequest):
  if request.method == "POST":
    new_plant = Plant(name= request.POST['name'], about= request.POST['about'], user_for= request.POST['user_for'], category = request.POST['category'], is_edible= request.POST['is_edible'], image= request.FILES['image'])
    new_plant.save()
    return redirect("main:home_page_view")
  return render(request, "plants/create_plant.html", {"CategoryChoices": Plant.CategoryChoices.choices})

# <!-- 
#   category = models.CharField(max_length= 20 ,choices=CategoryChoices.choices)
# -->