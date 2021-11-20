from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

class LogIn(forms.Form):
    name  = forms.CharField(label="Name",max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User