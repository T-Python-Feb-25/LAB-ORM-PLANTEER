from django.shortcuts import render, redirect
from Plants.models import Plant


def home(request):
    plants = Plant.objects.all()[:2]  
    return render(request, 'home.html', {'plants': plants})


