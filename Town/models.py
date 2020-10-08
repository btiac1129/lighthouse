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