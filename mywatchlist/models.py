from django.db import models

class ItemWatchlist(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()
