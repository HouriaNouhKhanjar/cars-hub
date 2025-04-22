from cloudinary.models import CloudinaryField
import cloudinary.uploader
from urllib.parse import urlparse
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
import os


APPROVED = ((0, "Not Approved"), (1, "Approved"))


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
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["created_on"]

        
class Car(models.Model):
    """
    Car model title, model, brand, age, category, owner, approved, created_on,
    description
    """
    title = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    age = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="user_cars")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="category_cars")
    approved = models.IntegerField(choices=APPROVED, default=0)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} | created on: {self.created_on.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ["-created_on"]
        

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', default='placeholder')
    
    def get_cloudinary_public_id(self):
        """
        Extract Cloudinary public ID from the image URL.
        """
        try:
            url = self.image.url
            path = urlparse(url).path  # e.g., /v1/car_images/filename.jpg
            public_id = os.path.splitext(path)[0].strip('/')  # removes extension
            return public_id
        except Exception as e:
            print("Failed to extract public ID:", e)
            return None

    def __str__(self):
        return f"{self.get_cloudinary_public_id()}"


@receiver(post_delete, sender=CarImage)
def delete_cloudinary_image(sender, instance, **kwargs):
    if instance.image:
        public_id = instance.get_cloudinary_public_id()
        if public_id:
            cloudinary.uploader.destroy(public_id)