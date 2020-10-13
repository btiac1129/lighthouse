from django import forms
from .models import Town

class TownCreationForm(forms.ModelForm):
    class Meta:
        model = Town
        fields = ['name', 'description', 'thumbnail']