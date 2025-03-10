from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Conatct
# Create your views here.

# Contact Page 

def contact_page_view(request: HttpRequest):
    if request.method == "POST":
      new_contact_meassge = Conatct(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], message = request.POST['message'],)
      new_contact_meassge.save()
      return redirect("main:home_page_view")
    return render(request, "contact/contact.html")

# Contact Page 

def contact_messages_page_view(request: HttpRequest):
  messages = Conatct.objects.all()

  return render(request, "contact/contact_messages.html", {"messages":messages})

