from django import forms
from Holeapp.models import Product

class EMIFORM(forms.ModelForm):
    Product_Name=forms.CharField(disabled=True)
    Company_name=forms.CharField(disabled=True)
    Price=forms.CharField(disabled=True)
    class Meta:
        model=Product
        fields=['prod_name','name','price']