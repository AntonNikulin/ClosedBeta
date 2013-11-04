from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserRating(models.Model):
    rating = models.PositiveIntegerField(max_length=2)
    user = models.ForeignKey(User)
    game = models.ForeignKey("Game")

    def __unicode__(self):
        return "%s" % self.rating


class Game(models.Model):
    title = models.CharField(max_length=150, blank=False)
    release_date = models.DateField()
    genre = models.ManyToManyField("Genre")
    userRating = models.ManyToManyField(User, through="UserRating")
    rating = models.IntegerField()
    rating_voters = models.IntegerField()

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.genre

