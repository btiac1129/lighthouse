from django.contrib import admin
from .models import Town

@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'operator']