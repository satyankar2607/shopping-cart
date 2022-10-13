from django.db import models

class contestant(models.Model):
    email = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
