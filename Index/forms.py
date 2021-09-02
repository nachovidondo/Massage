
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput

class Contactform(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Name'}
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Email Adress'}
    ))
    content = forms.CharField(required= True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Message'}
    ))


