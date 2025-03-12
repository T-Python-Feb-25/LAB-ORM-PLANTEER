from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def base(request:HttpRequest):
    return render (request, 'main/base.html')

def home(request:HttpRequest):
    return render (request, 'main/home.html')

def contact_us(request:HttpRequest):
    return render(request, 'main/contact.html')

def contact_us_messages(request:HttpRequest):
    return render(request , 'main/contact_message.html')
