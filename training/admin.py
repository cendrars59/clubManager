from django.contrib import admin

from .models import Category, Practice

admin.site.register(Practice)
admin.site.register(Category)
