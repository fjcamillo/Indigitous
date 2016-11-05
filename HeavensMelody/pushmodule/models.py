from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars
# Create your models here.

class create(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateField(default=timezone.now)
    username = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    lyrics = models.TextField(max_length=3000)
    beat = models.FileField(blank=None, null=True)
    story = models.TextField(max_length=2000)
    photos = models.ImageField(blank=None, null=True)

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



