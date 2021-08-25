from django.contrib import admin

from .models import Card, Learning_history, Package

# Register your models here.

admin.site.register(Card)
admin.site.register(Learning_history)
admin.site.register(Package)