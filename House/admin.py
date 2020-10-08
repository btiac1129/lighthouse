from django.contrib import admin
from .models import House, Condition

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = [
        'town',
        'town_name',
        'title',
        'description',
        'date_started',
        'date_finished',
        'session',
        'is_completed',
        'created_at',
        'updated_at', 
        'builder'
    ]

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'condition'
    ]