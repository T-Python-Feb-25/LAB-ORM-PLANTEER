from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plants
# Create your views here.

def index(request:HttpRequest):

    plant = Plants.objects.all()[0:3]
    return render(request,'main/index.html' , {"plant" : plant})