from django.contrib import admin
from .models import Town, House, Condition

@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['town', 'town_name', 'town', 'description', 'date_started', 'date_finished', 'is_completed', 'created_at', 'updated_at']

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['title', 'condition']