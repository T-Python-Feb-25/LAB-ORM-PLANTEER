from django.shortcuts import render,redirect
from .models import Plant, Comment

# Create your views here.
from django.http import HttpRequest, HttpResponse
# Create your views here.
def all_plants_view(request : HttpRequest):
	plants = Plant.objects.all()

	is_edible = request.GET.get('is_edible')
	if is_edible:
		plants = plants.filter(is_edible=is_edible)

	category = request.GET.get('category')
	if category:
		plants = plants.filter(category=category)

	return render(request,'plants/all_plants.html',{"plants": plants})

def create_plants_view(request : HttpRequest):
	if request.method == "POST":
		new_plant=Plant(name=request.POST['name'],about=request.POST['about'],used_for=request.POST['used_for'],category=request.POST['category'],is_edible=request.POST['is_edible'],image=request.FILES['image'])
		new_plant.save()
		return redirect('plants:all_plants_view')
	return render(request,'plants/create_plant.html')





def plant_detail_view(request: HttpRequest, plant_id:int):
	plants = Plant.objects.get(pk=plant_id)
	comments = Comment.objects.filter(plant=plants)

	realated_plants=Plant.objects.filter(category=plants.category)[0:3]

	return render(request, "plants/plant_detail.html", {"plants": plants, "comments": comments, "realated_plants": realated_plants})


def plant_update_view(request: HttpRequest, plant_id:int):
	plants = Plant.objects.get(pk=plant_id)
	if request.method == "POST":
		plants.name = request.POST['name']
		plants.about = request.POST['about']
		plants.used_for = request.POST['used_for']
		plants.category = request.POST['category']
		plants.is_edible = request.POST['is_edible']
		if 'image' in request.FILES:
			plants.image = request.FILES['image']
		plants.save()
		return redirect('plants:plant_detail_view', plant_id)
	return render(request, "plants/plant_update.html", {"plants": plants})



def plant_delete_view(request: HttpRequest, plant_id: int):
    plants = Plant.objects.get(pk=plant_id)
    plants.delete()
    return redirect('plants:all_plants_view')

def plant_search_view(request: HttpRequest):
	if 'search' in request.GET and len(request.GET['search'])>=3:
		plants = Plant.objects.filter(name__icontains=request.GET['search'])

	else:
		plants = []
	return render(request, "plants/plant_search.html", {"plants": plants})



def add_comment_view(request:HttpRequest, plant_id):

    if request.method == "POST":
        comment_object = Plant.objects.get(pk=plant_id)
        new_comment = Comment(plant=comment_object,plant_relation =request.POST['plant_relation'],full_name=request.POST['full_name'],content=request.POST['content'])
        new_comment.save()

    return redirect("plants:plant_detail_view", plant_id=plant_id)
