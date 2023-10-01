from django.core.validators import RegexValidator, MinLengthValidator
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=15, blank=False, null=False,
                                validators=[MinLengthValidator(2),
                                            RegexValidator(
                                            regex=r'^[a-zA-Z0-9_]+$',
                                            message='Ensure this value contains only letters, numbers, and underscore.'
                                                            )
                                            ]
                                )
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    password = models.CharField(max_length=20)

