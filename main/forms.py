from django import forms

class DanceForm(forms.Form):
    name = forms.CharField(max_length=100)
