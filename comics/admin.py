from django.contrib import admin

from .models import Comic, People, Publisher

admin.site.register(Comic)
admin.site.register(People)
admin.site.register(Publisher)
