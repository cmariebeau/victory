# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_unauthenticated_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='soundcloud_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
