from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('contact',views.contact,name='contact info'),
    path('database/',views.database),
    #path('database/create/',views.create),
    path('database/<str:dp>', views.department_data),
    

]
