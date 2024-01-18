from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.

class UserModel(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # username=models.CharField(max_length=70,unique=True)
    designation=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=70)
    objects = CustomUserManager()
    # USERNAME_FIELD=username
    REQUIRED_FIELDS=[]

    