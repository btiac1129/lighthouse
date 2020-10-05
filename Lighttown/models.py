from django.db import models

class Town(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class House(models.Model):
    town = models.ForeignKey(Town, on_delete=models.SET()) # FIXME:
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    date_started = models.DateTimeField()
    date_finished = models.DateTimeField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.title 
    
class Condition(models.Model):
    title = models.ForeignKey(House, on_delete=models.CASCADE)
    condition = models.CharField(max_length=300)

