# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pushmodule', '0004_auto_20161105_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='filter',
            field=models.IntegerField(choices=[(1, 'Art Punk'), (2, 'Alternative Rock'), (3, 'College Rock')], default=1),
        ),
    ]