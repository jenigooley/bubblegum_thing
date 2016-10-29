from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


class Comic(models.Model):

    series = models.CharField(max_length=200)
    issue_number = models.CharField(max_length=4)
    issue_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200)
    cover_art = models.URLField(max_length=500)
    writer = models.ForeignKey('People', related_name='writerpeople', max_length=200)
    artist = models.ForeignKey('People', related_name='artistpeople', max_length=200)
    letterer = models.ForeignKey('People', related_name='lettererpeople', max_length=200)
    publisher = models.ForeignKey('Publisher', max_length=200)
    cover_date = models.DateField('date published')
    notes = models.CharField(max_length=1000, null=True, blank=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Comic._meta.fields]

    def __str__(self):
        return self.series

    def was_published_recently(self):
        return self.cover_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('comic-detail', kwargs={'pk': self.pk})


class People(models.Model):
    name = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people-detail', kwargs={'pk': self.pk})

class Publisher(models.Model):
    publisher = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.publisher

    def get_absolute_url(self):
        return reverse('publisher-detail', kwargs={'pk': self.pk})
