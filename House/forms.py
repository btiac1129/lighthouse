from django import forms
from .models import House, Condition

class HouseCreationForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'description', 'date_started', 'session']

