from django.db import models

# Create your models here.

###
class Person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    birthdate=models.DateField(auto_now=False, auto_now_add=False)
    role=models.CharField(max_length=10)
