from django import forms
from plants.models import Plant,Comment,Contact

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields="__all__"
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['full_name', 'content']
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ['first_name',"last_name",'email','message']

