from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


# Home page view
def home_view(request):
    return render(request, 'main/home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            messages.success(request, 'Your message has been sent successfully!')  # Optional: Add a success message
            return redirect('home')  # Redirect to the home page
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})



def contact_messages(request):
    all_messages = Contact.objects.all().order_by('-created_at')  # Fetch all messages, ordered by date (newest first)
    return render(request, 'main/contact_messages.html', {'messages': all_messages})

def contact_message_detail(request, message_id):
    message = get_object_or_404(Contact, id=message_id)
    return render(request, 'main/contact_message_detail.html', {'message': message})
