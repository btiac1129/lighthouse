from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.template.loader import render_to_string

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

    def send_welcome_email(self):
        subject = render_to_string('accounts/welcome_email_subject.txt', {
            'user': self,
        })
        content =  render_to_string('accounts/welcome_email_content.txt', {
            'user': self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)

class Department(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name