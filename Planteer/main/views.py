from django.shortcuts import render



from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from plants.models import Plant


def main_view(request : HttpRequest):
    plants=Plant.objects.all()[0:3]

    return render(request, 'main/main_page.html',{'plants':plants} )