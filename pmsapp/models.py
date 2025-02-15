from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    emp_code=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    emp_code=models.OneToOneField(Login,on_delete=models.CASCADE,to_field='emp_code')
    kra_id=models.ManyToManyField('Kra',related_name='user')
    poa_id =models.ForeignKey('PlanOfAction',on_delete=models.CASCADE, null=True, blank=True)
    year=models.IntegerField()
    answer=models.TextField()
    user_rating =models.FloatField(default=0.0) 
    is_active=models.BooleanField(default=True)
    primary_reviewer_id =models.IntegerField()
    secondary_reviewer_id=models.IntegerField()

    def __str__(self):
        return f'User {self.user_id}'

class KraId(models.Model):
    id=models.AutoField(primary_key=True)
    year=models.IntegerField()
    department=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    

class Kra(models.Model):
    id=models.AutoField(primary_key=True)
    kra_id=models.ForeignKey(KraId,max_length=100,on_delete=models.CASCADE)
    kra_questions=models.TextField(null=True)
    answer_type=models.CharField(max_length=50)
    activate=models.BooleanField(default=True)
    added_on=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=255)

    
    def __str__(self):
        return str(self.kra_id)
    


class PlanOfAction(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    poa=models.TextField(blank=True)
    poa_points=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    year=models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=255)

    def __str__(self):
        return f'POA for {self.id} for user {self.user_id}'