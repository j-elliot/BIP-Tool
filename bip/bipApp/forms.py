from dal import autocomplete
from django import forms
from .models import Item



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')
        widgets = {
            'name': autocomplete.ModelSelect2(url='item-autocomplete')
        }
