from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
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
    mobile = models.CharField(max_length=255, default='(+000)0000000')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=True)
    profile_pic = models.ImageField(
        upload_to='customers',
        default="default.jpg", null=True, blank=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """Return string representation of the Customer object"""

        return f'{self.id}'
