from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import validator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            validator,
            MinLengthValidator(USERNAME_MIN_LENGTH),

        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )


class Album(models.Model):
    ALBUM_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RnB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, RnB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    name = models.CharField(
        unique=True,
        max_length=ALBUM_MAX_LENGTH,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=TYPES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
