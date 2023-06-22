from django.db import models
from django.core.validators import MinValueValidator

from My_Music_App.user_profile.models import Profile


# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    artist = models.CharField(max_length=30, blank=False, null=False)
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
    genre = models.CharField(max_length=30, blank=False, null=False, choices=some_choices)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0.0)])

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
