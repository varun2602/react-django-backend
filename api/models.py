from django.db import models
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank = True, null = True)

    def __str__(self):
        return self.username
