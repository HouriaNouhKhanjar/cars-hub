from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    User Profile model : Each user has a profile
    he can update it any time after login
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,
                                related_name="user_profile")
    profile_image = CloudinaryField('image', default='profile-placeholder')
    phone = models.CharField(max_length=20, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    """
    Car Category model
    """
    name = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} | created on: {self.created_on.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ["created_on"]