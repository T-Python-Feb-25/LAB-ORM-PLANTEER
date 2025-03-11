from django import forms
from plants.models import Plants

# Create the form class.
class PlantsForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput({"class" : "form-control"})
        }