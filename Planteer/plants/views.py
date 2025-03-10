from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Plant,Comment,Contact
from .forms import PlantForm ,CommentForm,ContactForm


def create_view(request:HttpRequest):
    if request.method=="POST":
        plant_form=PlantForm(request.POST,request.FILES)
        if plant_form.is_valid():
            print(plant_form)
            plant_form.save()
            return redirect('main:home_view')
        
    return render(request,"plants/add.html",{"catagory":Plant.CategoryChoice.choices})
def search_view(request:HttpRequest):
    if 'search' in request.GET and len(request.GET["search"])>2:
        plants=Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plants=[]
    return render(request,"plants/search.html",{"plants":plants})

def all_plants_view(request:HttpRequest):
    category=request.GET.get("category","")
    is_edible=request.GET.get("is_edible","")

    plants=Plant.objects.all()

    if category:
        plants=plants.filter(category=category)
    if is_edible:
        plants=plants.filter(is_edible=is_edible)

    return render(request,"plants/all_plants.html",{"plants":plants})
def plant_detail_view(request:HttpRequest,plant_id:int):
    plant=Plant.objects.get(pk=plant_id)
    user_comments = Comment.objects.filter(plant=plant)
    same_category = Plant.objects.filter(category=plant.category).exclude(pk=plant.pk).order_by('?')
    related_plant = list(same_category[:3])

    return render(request,"plants/detail.html",{"plant":plant,"comments":user_comments,"related_plant":related_plant})
def update_view(request:HttpRequest,plant_id):
    plant=Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        plant_form=PlantForm(instance=plant,data=request.POST,files=request.FILES)
        plant_form.save()
        return redirect("plants:plant_detail_view",plant_id=plant_id)

    return render(request,"plants/update.html",{"plant":plant,"catagory":Plant.CategoryChoice.choices})
def delate_view(request:HttpRequest,plant_id):
    plant=Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect("main:home_view")

def add_comment_view(request:HttpRequest,plant_id:int):
    plant=Plant.objects.get(pk=plant_id)
    if request.method=="POST":
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():

            comment=form.save(commit=False)
            comment.plant=plant
            comment.save()
            return redirect('plants:plant_detail_view', plant_id=plant_id)

def contact_us_view(request:HttpRequest):
    return render(request,'plants/contact.html')
def add_contact_us_view(request:HttpRequest):
    if request.method=="POST":
        contact_form=ContactForm(request.POST,request.FILES)
        if contact_form.is_valid():

            contact_form.save()
    return redirect('main:home_view')
        
def contact_us_all_view(request:HttpRequest):
    contact_us=Contact.objects.all()
    return render(request,"plants/all_contact_us.html",{"messages":contact_us})