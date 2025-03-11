from django.shortcuts import render, redirect

from .models import Contact
# Create your views here.

from django.http import HttpRequest, HttpResponse
# Create your views here.
def contact_us_view(request : HttpRequest):
	if request.method == "POST":
		new_contact = Contact(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],message=request.POST['message'])
		new_contact.save()
		return redirect('contact:contact_us_view')
	return render(request, "contact_us.html", )


def contact_us_messages_view(request : HttpRequest):
	contacts = Contact.objects.all()
	return render(request, "contact_us_message.html",{"contacts":contacts})