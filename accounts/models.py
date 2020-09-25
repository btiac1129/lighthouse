from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("M", "Male")
        FEMAIL = ("F", "Female")

    department_set = models.ManyToManyField('Department')
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    # lighthouses

    @property
    def name(self):
        return f"(self.first_name) (self.last_name)"

class Department(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name