from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']
        widgets = {
            'is_edible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }