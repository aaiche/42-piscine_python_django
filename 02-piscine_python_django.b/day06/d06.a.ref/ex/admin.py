from django.contrib import admin
from .models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    fields = ['username', 'password',]

admin.site.register(MyUser, MyUserAdmin)
