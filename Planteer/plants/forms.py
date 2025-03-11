from django import forms
from .models import Plant, Comment


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'category', 'is_edible', 'description', 'image', 'related_plants']
        widgets = {
            'related_plants': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Use a multi-select dropdown
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the default value to null (empty option)
        self.fields['related_plants'].empty_label = "Select related plants (optional)"
        self.fields['related_plants'].required = False  # Make the field optional

        # Show all plants in the related_plants dropdown
        self.fields['related_plants'].queryset = Plant.objects.all()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 4}),
        }

