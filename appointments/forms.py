from django import forms
from .models import Quote


class NewQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'phone', 'email', 'category', 'area', 'address', 'pincode' ]