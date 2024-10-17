# your_app_name/models.py
from django.db import models

class Info(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Ensure username is unique
    phone = models.CharField(max_length=15)  # Updated max_length for phone number
    password = models.CharField(max_length=255)  # Consider using a hashed password

    def __str__(self):
        return self.username
