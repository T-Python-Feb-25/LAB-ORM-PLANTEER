from django.shortcuts import render



# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

from django.shortcuts import render
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

       
        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, 'core/contact.html')



from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')



