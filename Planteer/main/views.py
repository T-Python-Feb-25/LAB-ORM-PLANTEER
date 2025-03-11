from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_messages')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def contact_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})



# Create your views here.
