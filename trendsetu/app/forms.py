from django import forms
from .models import ClothingProduct  # Make sure this matches your actual model name

class ClothingForm(forms.ModelForm):
    class Meta:
        model = ClothingProduct
        fields = ['title', 'brand', 'size', 'price', 'description', 'category', 'color', 'image']