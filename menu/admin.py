from django.contrib import admin
from .models import MenuItem, Menu, Category
# Register your models here.
admin.site.register([MenuItem, Menu, Category])