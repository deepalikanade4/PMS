from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.

class UserModel(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # username=models.CharField(max_length=70,unique=True)
    last_name=None
    first_name=None

    designation=models.CharField(max_length=250)
    email=models.EmailField(max_length=350)
    # password=models.CharField(max_length=250)
    objects = CustomUserManager()
    # USERNAME_FIELD=username
    REQUIRED_FIELDS=[]

    