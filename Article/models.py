from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    Title = models.CharField(max_length=200)
    Body = models.TextField()
    Author = models.ForeignKey(User)
    Date_created = models.DateTimeField(auto_now_add=True)
    Date_modified = models.DateTimeField(auto_now=True)
    Points = models.IntegerField(default=1)
    Voters = models.ForeignKey(User)


class Tag(models.Model):
    Name = models.CharField(max_length=50)
    Articles = models.ManyToManyField(Article)