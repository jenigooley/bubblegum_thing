
import random
import string

from django.test import TestCase
import datetime

from django.utils import timezone
from django.test import Client

from .models import *

import factories


# class BaseTestCase(TestCase):

#     def user(self, name):
#         user =User.objects.create(username=name)
#         user.set_password('password')
#         user.save()
#         self.user_pk = user.pk
#         return user
    
#     def login(self, pk):
#         self.client = Client()
#         user = User.objects.get(pk=pk)
#         name = user.username
#         logged_in = self.client.login(username=name, password='password')
#         self.assertTrue(logged_in)

#     def comic(self, series):
#         comic = Comic.objects.create()
class ComicTestCase(TestCase):
    def test_if_comic_is_displayed(self):
        category = factories.ComicFactory.create()

        response = self.client.get('/')
        self.assertTrue(comic.series in response.content)



    def test_comic(self):
        # Get a completely random thing
        thing = ComicFactory.create()
        # Test assertions would go here
        