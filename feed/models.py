from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=450)
    date = models.DateTimeField('date published', default=datetime.date(2000, 1, 1))

class Name(models.Model):
    usern = models.CharField(max_length=30)
