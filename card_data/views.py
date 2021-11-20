from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User # User =see and create user data in database, auth for authentication
#from django.contrib import auth
from .models import IdCard

# Create your views here.

def home(request):
    return render(request,'card_data/home.html',{})



def contact(request):
    return render(request,'card_data/contact.html',{})

def database(request):
    data=IdCard.objects.values()
    return render(request,'card_data/database.html',{'data':data})    