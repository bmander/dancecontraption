from django import forms
from django.forms import ModelForm
from models import Event, Band
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DanceForm(forms.Form):
    name = forms.CharField(max_length=100)

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['dance']

class BandForm(ModelForm):
    class Meta:
        model = Band

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class UserCreationWithNameForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
