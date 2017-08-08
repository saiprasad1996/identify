from django.db import models

# Create your models here.
class Identity(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profession = models.TextField(default="")
    picture = models.ImageField(upload_to='media/profilepics')
    facebook = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    googleplus = models.CharField(max_length=100)
    govtid = models.CharField(max_length=80)

