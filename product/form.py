from django import forms

from .models import Product, Purchase

class Purchaseform(forms.ModelForm):
    product=forms.ModelChoiceField(queryset=Product.objects.all(),
                        label='Product',
                        widget=forms.Select(attrs={'class':'ui selection dropdown'}))
    class Meta():
        model=Purchase
        fields=['product','price','quantity']

