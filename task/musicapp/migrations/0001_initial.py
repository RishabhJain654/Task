# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import musicapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('rating', musicapp.models.IntegerRangeField()),
            ],
            options={
                'db_table': 'tracks',
            },
        ),
    ]
