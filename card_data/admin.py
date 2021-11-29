from django.contrib import admin
from .models import IdCard,Department,UserInfo
# Register your models here.

admin.site.register(IdCard)
admin.site.register(Department)
admin.site.register(UserInfo)