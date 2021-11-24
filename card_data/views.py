from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User # User =see and create user data in database, auth for authentication
#from django.contrib import auth
from .models import IdCard, Department



# Create your views here.

def home(request):
    return render(request,'card_data/home.html',{})


def contact(request):
    return render(request,'card_data/contact.html',{})


# მონაცემთა ბაზის ფუნქცია, გამოაქვს დეპარტამენტების სია
def database(request):
    #card = IdCard.objects.filter(department=department) 
    department = Department.objects.values('department')
    return render(request,'card_data/database.html',{'department':department})

# არჩეულ დეპარტამენტიდან გამოაქვს იმ ადამიანების სია ვინც მასშია
def department_data(request,dp):
    dep = Department.objects.filter(department=dp).values('id')
    dep_id = [item['id'] for item in dep]

    data_list = IdCard.objects.filter(department_id=dep_id[0])

    return render(request,'card_data/department_data.html',{'data_list':data_list})


# ადამიანთა სიიდან რომელიმის არჩევის შემთხვევაში გამოაქვს მისი მთლიანი მინაცემები 
def single_id(request,id,dp):
    dp = 'dp'
    card = IdCard.objects.get(id=id)#,last_name=last_name)
    return render(request,'card_data/single_id.html',{'card':card})







