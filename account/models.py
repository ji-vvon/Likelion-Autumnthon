from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500, null=True)
    coin=models.IntegerField(null=True)
