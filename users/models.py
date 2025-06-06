from datetime import datetime
import re

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)

    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    # profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    # username = models.CharField(max_length=150, unique=True, blank=False)
    # password = models.CharField(max_length=128, blank=False)
    # email = models.EmailField(unique=True)
    # is_active = models.BooleanField(default=True)
    # # date_joined = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # last_login = models.DateTimeField(default=datetime.now, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __init__(self, *args, **kwargs):
        """
        Initialize the Users model with custom fields.
        """
        super().__init__(*args, **kwargs)
        self.name = self.get_full_name()
        self.short_name = self.get_short_name()

    def __repr__(self):
        return f"<User: {self.email}>"
    
    def __str__(self):
        return self.email
    
    def get_profile_pic_url(self):
        """
        Return the URL of the user's profile picture.
        """
        if self.profile_pic:
            return self.profile_pic.url
        return None
    
    def get_absolute_url(self):
        """
        Return the absolute URL for the user.
        """
        return f"/users/{self.pk}/"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
