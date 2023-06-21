from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    some_choices = (
        ('1', "Pop Music"),
        ('2', "Jazz Music"),
        ('3', "R&B Music"),
        ('4', "Rock Music"),
        ('5', "Country Music"),
        ('6', "Dance Music"),
        ('7', "Hip Hop Music"),
        ('8', "Other")
    )
    genre = models.CharField(max_length=30, choices=some_choices)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=False)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0)])
