from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class create(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateField(default=timezone.now())
    username = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    lyrics = models.TextField(max_length=3000)
    beat = models.FileField()
    story = models.TextField(max_length=2000)
    photos = models.ImageField()

    def __str__(self):
        return self.title


