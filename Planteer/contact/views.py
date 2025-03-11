from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from .forms import ContactForm
# Create your views here.
def contact_view(request: HttpRequest):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            #return redirect('contact_success')  
        else:
            return HttpResponse('Invalid form')
    return render(request, 'contact/contact.html', {'contact_form': contact_form})

def contact_success(request: HttpRequest):
    return render(request, 'contact/contact_success.html')


def contact_messages_view(request: HttpRequest):
    messages = Contact.objects.all()
    return render(request, 'contact/contact_messages.html', {'messages': messages})
