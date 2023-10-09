from django.db import models

from My_Music_App.album.models import Album


# Create your models here.


class Songs(models.Model):
    name = models.CharField(max_length=50)
    length = models.TimeField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

