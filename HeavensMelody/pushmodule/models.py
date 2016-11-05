from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars
# Create your models here.

class create(models.Model):

    genre_art_punk = 1
    genre_alternative_rock = 2
    genre_college_rock = 3
    genre_crossover_thrash = 4
    genre_crust_punk = 5
    genre_experimental_rock = 6
    genre_hardcore_punk = 7
    genre_acoustic_blues = 8
    genre_indie_rock = 9
    genre_chamber_music = 10

    types_of_genre = (
        (genre_art_punk, 'Art Punk'),
        (genre_alternative_rock, 'Alternative Rock'),
        (genre_college_rock, 'College Rock'),
        (genre_crossover_thrash, 'Cross Over Thras'),
        (genre_crust_punk, 'Crust Punk'),
        (genre_experimental_rock, 'Experimental Rock'),
        (genre_hardcore_punk, 'Hard Core Punk'),
        (genre_acoustic_blues, 'Acoustic Blues'),
        (genre_indie_rock, 'Indie Rock'),
        (genre_chamber_music, 'Chamber Music'),
    )

    title = models.CharField(max_length=50)
    time = models.DateField(default=timezone.now)
    username = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    lyrics = models.TextField(max_length=3000)
    beat = models.FileField(blank=None, null=True)
    story = models.TextField(max_length=2000)
    photos = models.ImageField(blank=None, null=True)
    filter = models.IntegerField(choices=types_of_genre, default=1)

    def __str__(self):
        return self.title
    
    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    @property
    def short_lyrics(self):
        return truncatechars(self.lyrics, 100)

    @property
    def short_story(self):
        return truncatechars(self.story, 100)





