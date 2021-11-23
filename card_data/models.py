from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class IdCard(models.Model):
    first_name  = models.CharField(max_length=120,null=False)
    last_name   = models.CharField(max_length=120,null=False)
    personal_no = models.CharField(max_length=11,null=False,unique=True)
    birth_place = models.CharField(max_length=120,null=False)
    birth_date  = models.DateField()
    sex         = models.CharField(null=False,choices=(('f','female'),('m','male')),max_length=20)
    photo       = models.ImageField(upload_to='images/')
    department  = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    drivers_license = models.CharField(max_length=20, null=False, choices =(('Yes','Yes'),('No','No')))


    def __str__(self):
        return f'{self.first_name} {self.last_name}  {self.personal_no}'


    def clean(self):
        if not self.personal_no.isnumeric() :
            raise ValidationError(
                "Personal ID Number should be numbers!")
        
        if not self.first_name.isalpha() or  not self.last_name.isalpha():
            raise ValidationError(
                "First Name and Last Name should be letters!") 



class Department(models.Model):
    
    department = models.CharField(max_length=120,unique=True,null=False)

    def __str__(self):
        return self.department

