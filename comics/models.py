from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Comic(models.Model):
    series = models.CharField(max_length=200)
    issue_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cover_art = models.URLField(max_length=500)
    writer = models.ForeignKey('People', related_name='writerpeople', max_length=200)
    artist = models.ForeignKey('People', related_name='artistpeople', max_length=200)
    letterer = models.ForeignKey('People', related_name='lettererpeople', max_length=200)
    publisher = models.ForeignKey('Publisher', max_length=200)
    cover_date = models.DateTimeField('date published')

    def __str__(self):
        return self.series

    def was_published_recently(self):
        return self.cover_date >= timezone.now() - datetime.timedelta(days=1)


class People(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
