from django import  forms
from .models import Customer

class customer_register(forms.ModelForm):
    class Meta():
        model=Customer
        fields=['company_name','budget','employment']