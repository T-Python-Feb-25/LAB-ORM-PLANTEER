from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


# Home Page Page
def home_page_view(request :HttpRequest):
  return render(request, "main/index.html")

# All Plants Page
def all_plants_view(request :HttpRequest):
  pass

# Plant Detail Page
def plant_detail_view(request :HttpRequest):
  pass
