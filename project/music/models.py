from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    release_date = models.IntegerField()
    num_stars = models.IntegerField()
