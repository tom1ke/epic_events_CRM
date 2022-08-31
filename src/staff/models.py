from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'ADMIN'),
        ('SALES', 'SALES'),
        ('SUPPORT', 'SUPPORT')
    ]

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
