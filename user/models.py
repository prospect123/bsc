from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    Email = models.EmailField(null=True)
    mobile_no = models.IntegerField(null=True,blank=True)
    Address = models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True,blank=True)
