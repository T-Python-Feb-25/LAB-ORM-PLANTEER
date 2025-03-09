from django.shortcuts import render
from .models import Plant
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def plant(request):
    return render(request, 'main/plant.html')

def detail(request):
    return render(request, 'main/detail.html')

def add(request):
    return render(request, 'main/add.html')

def update(request):
    return render(request, 'main/update.html')

def delete(request):
    return render(request, 'main/delete.html')

def search(request):
    return render(request, 'main/search.html')
