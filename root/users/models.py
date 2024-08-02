from root.utils import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from .managers import CustomUserManager

class User(BaseModel,  AbstractUser):
    username = models.CharField(max_length=100, unique = True)
    phone_number = models.CharField(max_length=100, unique = True, null = True, blank = True)
    phone_number_verified = models.BooleanField(default = False)
    email = models.EmailField(max_length=100, unique = True, null = True, blank = True)
    user_image = models.ImageField(upload_to = "user/profile", null = True, blank = True)
    full_name = models.CharField(max_length=100, null = True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"
    

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "user_profile")
    bio = models.TextField(blank = True)

    def __str__(self):
        return f"{self.user.username}"