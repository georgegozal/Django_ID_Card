from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import IdCard, Department


def home(request):
    return render(request,'card_data/home.html',{})

def contact(request):
    return render(request,'card_data/contact.html',{})


# მონაცემთა ბაზის ფუნქცია, გამოაქვს დეპარტამენტების სია
@login_required(login_url="/login/")
def database(request):
    department = Department.objects.values('department')
    return render(request,'card_data/database.html',{'department':department})

# არჩეულ დეპარტამენტიდან გამოაქვს იმ ადამიანების სია ვინც მასშია
def department_data(request,dp):
    dep = Department.objects.filter(department=dp).values('id')
    dep_id = [item['id'] for item in dep]

    data_list = IdCard.objects.filter(department_id=dep_id[0])

    return render(request,'card_data/department_data.html',{'data_list':data_list})





