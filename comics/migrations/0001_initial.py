# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=200)),
                ('issue_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('cover_art', models.URLField(max_length=500)),
                ('cover_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='artist',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='artistpeople', to='comics.People'),
        ),
        migrations.AddField(
            model_name='comic',
            name='letterer',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='lettererpeople', to='comics.People'),
        ),
        migrations.AddField(
            model_name='comic',
            name='publisher',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='comics.Publisher'),
        ),
        migrations.AddField(
            model_name='comic',
            name='writer',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='writerpeople', to='comics.People'),
        ),
    ]
