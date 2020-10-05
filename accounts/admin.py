from django.contrib import admin
from .models import User, Department

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']

@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
