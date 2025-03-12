#from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from .models import Plant, Comment , Category ,ContactMessage
from .forms import PlantForm 
 # Create your views here.

# def home_page (request : HttpRequest):
  
#     return render(request, 'app_planteer/home_page.html')



def home_page(request: HttpRequest):
   
    random_plants = Plant.objects.order_by('?')[:3]

    return render(request, 'app_planteer/home_page.html', {
        "random_plants": random_plants  
    })


def all_plants(request : HttpRequest):

   # planteer =Plant.objects.all()
   # return render(request, 'app_planteer/all_plants.html',{"planteer":planteer})

   
   
    categories = Category.objects.all()

   
    planteer = Plant.objects.all()

   
    category_filter = request.GET.get('category', 'all')
    is_edible_filter = request.GET.get('is_edible', 'all')


    if category_filter.isdigit() and Category.objects.filter(id=int(category_filter)).exists():
        planteer = planteer.filter(category__id=int(category_filter))

    if is_edible_filter == "true":
        planteer = planteer.filter(is_edible=True)

    return render(request, 'app_planteer/all_plants.html', {
        "planteer": planteer, 
        "categories": categories,  
        "selected_category": int(category_filter) if category_filter.isdigit() else None,
        "selected_is_edible": is_edible_filter,
    })




def add_plant(request : HttpRequest):

    if request.method=="POST":
       new_plant=Plant(name=request.POST["name"],description=request.POST["description"],poster=request.FILES["poster"])
       new_plant.save()
    #print(request.POST)
   
    return render(request, 'app_planteer/add_plant.html')




def search_plants(request: HttpRequest):
    query = request.GET.get("query", "").strip()  
    plants = Plant.objects.filter(name__icontains=query) if query else []  


    
    random_plants = Plant.objects.order_by('?')[:3]

    return render(request, 'app_planteer/search_plants.html', {
        "plants": plants,
        "query": query,
        "random_plants": random_plants 
    })



def contact(request: HttpRequest):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

       
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("app_planteer:contact_page_messages")  


    return render(request, 'app_planteer/contact.html')



def contact_page_messages(request: HttpRequest):
   
    messages = ContactMessage.objects.all().order_by('-sent_at')  

    return render(request, 'app_planteer/contact_page_messages.html', {"messages": messages})



def plant_detail(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)  
    
    if request.method == "POST":
        new_comment = Comment(
            plant=plant,  
            full_name=request.POST["full_name"],
            content=request.POST["comment"],
            created_at=timezone.now()
        )
        new_comment.save()
        return redirect('app_planteer:plant_detail', plant_id=plant.id)  

    comments = plant.comments.all()  
  
   
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:4]  

    return render(request, 'app_planteer/plant_detail.html', {
        "plant": plant,
        "comments": comments,
        "related_plants": related_plants  
    })




def plant_edit(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('app_planteer:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'app_planteer/plant_edit.html', {"form": form, "plant": plant})


def plant_delete(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)
    
    if request.method == "POST":
        plant.delete()
        return redirect('app_planteer:all_plants') 

    return render(request, 'app_planteer/plant_delete.html', {"plant": plant})