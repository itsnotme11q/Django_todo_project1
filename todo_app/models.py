from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    is_complete=models.BooleanField(default=False)
    todo=models.CharField(max_length=200)

    def __str__(self):
        return self.todo + ' -- >' 

class Login(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Register(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    confirm_password=models.CharField(max_length=25)