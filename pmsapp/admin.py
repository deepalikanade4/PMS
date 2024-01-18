from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserModel)
class adminusers(UserAdmin):

    model=UserModel
    # fields=['username','password','designation',]
    list_display=['username','password','designation','email']


