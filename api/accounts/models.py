from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns string representation of user object
        """
        return f'{self.username}'


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    profile_pic = models.ImageField(
        default="default.png", null=True, blank=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
