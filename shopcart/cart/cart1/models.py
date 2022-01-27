from django.db import models

class peop(models.Model):
    product = models.CharField(max_length=30,null = True)
    price = models.IntegerField(max_length=30,null = True)
class cartitem(models.Model):
    product = models.CharField(max_length=30, null=True)
    price = models.IntegerField(max_length=30, null=True)
class custdata(models.Model):
    email = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
