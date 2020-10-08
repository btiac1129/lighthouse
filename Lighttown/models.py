from django.db import models
from django.conf import settings
from datetime import timedelta

class Town(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class House(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    town_name = models.JSONField(null=True, blank=True) # FIXME:
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    date_started = models.DateTimeField(blank=True)
    date_finished = models.DateTimeField(blank=True)
    session = models.DurationField(default=timedelta(days=1))
    is_completed = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    builder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title 
    
class Condition(models.Model):
    title = models.ForeignKey(House, on_delete=models.CASCADE)
    condition = models.CharField(max_length=300)

    class Meta:
        ordering = ["id"]
