from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    Title = models.CharField(max_length=200)
    Body = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True)
    Date_modified = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    Name = models.CharField(max_length=50)
    Articles = models.ManyToManyField(Article)