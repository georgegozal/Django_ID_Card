from django import forms
#from django.db import models 

from django.core.exceptions import ValidationError

class CreateID(forms.Form):
    first_name  = forms.CharField(max_length=120)
    last_name   = forms.CharField(max_length=120)
    personal_no = forms.CharField(max_length=11)
    birth_place = forms.CharField(max_length=120)
    birth_date  = forms.DateField()
    sex         = forms.CharField(max_length=20)
    photo       = forms.ImageField()
    department  = forms.CharField(max_length=120)
    #drivers_license = forms.CharField(max_length=100, choices = (('აქვს','აქვს'),('არ აქვს', 'არ აქვს '))








#class DepartmentForm(forms.Form):
    
#    department = forms.CharField(max_length=120,unique=True,null=False)

#     def __str__(self):
#         return self.department

