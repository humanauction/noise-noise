from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    """Extended user model with additional fields"""
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class GuestSession(models.Model):
    """Track guest users with session tokens"""
    session_key = models.CharField(max_length=40, unique=True)
    guest_token = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Guest {self.guest_token}'
