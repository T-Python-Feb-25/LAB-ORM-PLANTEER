from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import  Plants 
# Create your views here.

def home_view(request:HttpRequest):
  plants = Plants.objects.filter()[0:3]
  return render(request, 'main/index.html', {'plants':plants})