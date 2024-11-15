from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='media/')
