from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('herb', 'Herb'),
        ('fruit', 'Fruit'),
        ('vegetable', 'Vegetable'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']  # Explicitly listing fields
