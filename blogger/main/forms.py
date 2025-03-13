from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    is_published = forms.BooleanField(
        initial=True,  # Default value is True
        required=False,  # Optional field
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}),
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'is_published']