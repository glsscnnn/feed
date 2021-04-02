from django.db import models
from django.conf import settings

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=450)

class Name(models.Model):
    usern = models.CharField(max_length=30)
