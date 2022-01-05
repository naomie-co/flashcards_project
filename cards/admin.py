from django.contrib import admin

from .models import Card, Learning_statistics, Package

# Register your models here.

admin.site.register(Card)
admin.site.register(Learning_statistics)
admin.site.register(Package)