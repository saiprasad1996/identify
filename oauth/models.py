from django.db import models

# Create your models here.
class Tokens:
    appname = models.CharField(max_length=100)
    appid = models.CharField(max_length=100,primary_key=True)
    accesstoken = models.TextField(unique=True)
    appsecret = models.TextField(unique=True)
    refreshtoken = models.TextField(unique=True)
    validity = models.DateTimeField(auto_now=True)
    resources = models.TextField(default='[]')