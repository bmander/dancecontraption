from django import forms
from django.forms import ModelForm
from models import Event

class DanceForm(forms.Form):
    name = forms.CharField(max_length=100)

class EventForm(ModelForm):
    class Meta:
        model = Event
