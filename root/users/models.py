from django.db import models

from root.utils import BaseModel
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class User(BaseModel,AbstractUser):
    username = models.CharField(max_length=100, unique = True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('author', 'Author'), ('reader', 'Reader')])
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"