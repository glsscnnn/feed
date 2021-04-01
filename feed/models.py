from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=450)
