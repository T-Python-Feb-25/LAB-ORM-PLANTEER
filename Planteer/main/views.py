from django.shortcuts import render
from .models import ContactMessage

def home(request):
    return render(request, 'main/home.html')

def contact(requst):
    return render(requst, 'main/contact.html')

def contact_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})


# Create your views here.
