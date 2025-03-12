from django.shortcuts import render,redirect
from django.http import HttpRequest
from plants.models import Plant
from .models import Contact
from .forms import  ContactForm

def home_view(requset:HttpRequest):

    plants=Plant.objects.all()[0:3]
    plants=Plant.objects.order_by("?")[:3]
    return render(requset,"main/home.html",{"plants":plants})
def contact_us_view(request:HttpRequest):
    return render(request,'main/contact.html')
def add_contact_us_view(request:HttpRequest):
    if request.method=="POST":
        contact_form=ContactForm(request.POST,request.FILES)
        if contact_form.is_valid():

            contact_form.save()
    return redirect('main:home_view')
        
def contact_us_all_view(request:HttpRequest):
    contact_us=Contact.objects.all()
    return render(request,"main/all_contact_us.html",{"messages":contact_us})