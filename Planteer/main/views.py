from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
# Create your views here.
def home_view(request:HttpRequest):
    plants = Plant.objects.all()[:3]
    print(plants)
    return render(request,'main/home.html',{'plants':plants} )

