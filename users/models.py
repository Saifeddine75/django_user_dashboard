from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
