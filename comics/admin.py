from django.contrib import admin

from .models import Comic, People, Publisher, UserComic

admin.site.register(Comic)
admin.site.register(People)
admin.site.register(Publisher)
admin.site.register(UserComic)
