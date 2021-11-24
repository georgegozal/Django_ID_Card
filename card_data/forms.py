from django import forms
#from django.db import models 

from django.core.exceptions import ValidationError

class CreateID(forms.Form):
    first_name  = forms.CharField(max_length=120,null=False)
    last_name   = forms.CharField(max_length=120,null=False)
    personal_no = forms.CharField(max_length=11,null=False,unique=True)
    birth_place = forms.CharField(max_length=120,null=False)
    birth_date  = forms.DateField()
    sex         = forms.CharField(null=False,choices=(('f','female'),('m','male')),max_length=20)
    photo       = forms.ImageField(upload_to='images/')
    department  = forms.ForeignKey('Department', on_delete=forms.SET_NULL, null=True)
    drivers_license = forms.CharField(max_length=20, null=False, choices =(('Yes','Yes'),('No','No')))


    def __str__(self):
        return f'{self.first_name} {self.last_name}  {self.personal_no}'


    def clean(self):
        if not self.personal_no.isnumeric() :
            raise ValidationError(
                "Personal ID Number should be numbers!")
        
        if not self.first_name.isalpha() or  not self.last_name.isalpha():
            raise ValidationError(
                "First Name and Last Name should be letters!") 



class DepartmentForm(forms.Form):
    
    department = forms.CharField(max_length=120,unique=True,null=False)

    def __str__(self):
        return self.department

