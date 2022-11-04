from django.contrib import admin

# Register your models here.
from .models import Category,Website

admin.site.register(Category)
admin.site.register(Website)