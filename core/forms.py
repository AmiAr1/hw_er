from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'photo']


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'photo']