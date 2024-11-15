from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='media/')
    twitter_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=100)

