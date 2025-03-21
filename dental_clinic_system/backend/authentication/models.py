from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrator'),
        ('dentist', 'Dentist'),
        ('assistant', 'Assistant'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='dentist')
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
