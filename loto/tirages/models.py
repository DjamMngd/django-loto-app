from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Fields inherited from AbstractUser
    # username, first_name, last_name, email, password
    # is_active, is_staff, is_superuser
    # last_login, date_joined

    # Additional fields
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # Ajouter les champs necessaires pour les tirages de loto