# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0029_auto_20170929_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='groups',
        ),
        migrations.AddField(
            model_name='group',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.Team'),
        ),
    ]
