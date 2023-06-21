from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=15,
                                validators=[
                                    RegexValidator(
                                        regex=r'^[a-zA-Z0-9_]+$',
                                        message='Ensure this value contains only letters, numbers, and underscore.'
                                                    )
                                            ]
                                )
    email = models.EmailField(blank=False)
    age = models.SmallIntegerField(blank=True, validators=[MinValueValidator(0)])
