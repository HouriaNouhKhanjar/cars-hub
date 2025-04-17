from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, 
                                related_name="user_profile")
    profile_image = CloudinaryField('image', default='profile-placeholder')
    phone = models.CharField(max_length=20, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

