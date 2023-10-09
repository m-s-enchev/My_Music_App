from django.db import models
from django.core.validators import MinValueValidator

from My_Music_App.user_profile.models import Profile


# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    artist = models.CharField(max_length=30, blank=False, null=False)
    some_choices = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    )
    genre = models.CharField(max_length=30, blank=False, null=False, choices=some_choices)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0.0)])

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def songs_in_album(self):
        id = self.songs_set.values_list('id', flat=True)
        name = self.songs_set.values_list('name', flat=True)
        concatenated_list = []
        for i in range(len(id)):
            element = f'{id[i]}. {name[i]}'
            concatenated_list.append(element)
        return concatenated_list


