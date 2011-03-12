from django import forms
from django.forms import ModelForm
from models import Event, Band
from django.contrib.auth.forms import UserCreationForm

class DanceForm(forms.Form):
    name = forms.CharField(max_length=100)

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['dance']

class BandForm(ModelForm):
    class Meta:
        model = Band

class UserCreationWithNameForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
