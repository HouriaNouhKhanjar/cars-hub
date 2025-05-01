from functools import cached_property
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.db.models.signals import post_delete
from urllib.parse import urlparse
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
import os
import re


APPROVED = ((0, "Not Approved"), (1, "Approved"))


class UserProfile(models.Model):
    """
    Stores a single profile entry related to :model:`auth.User`.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,
                                related_name="user_profile")
    profile_image = CloudinaryField('image', default='profile-placeholder')
    phone = models.CharField(max_length=20, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    @cached_property
    def image_url(self):
        url = self.profile_image.url
        # Replace http with https to improve performance
        if 'placeholder' not in url:
            return url.replace("http://", "https://")
        return '/static/images/nobody.webp'

    def __str__(self):
        return self.user.username


class Category(models.Model):
    """
    Stores a single category entry.
    """
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')

    @cached_property
    def image_url(self):
        url = self.image.url
        # Replace http with https to improve performance
        if 'placeholder' not in url:
            return url.replace("http://", "https://")
        return '/static/images/placeholder.webp'

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["created_on"]


class Car(models.Model):
    """
    Stores a single car entry related to model:`auth.User`
    and :model:`car.Category`.
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
    likes = models.ManyToManyField(User, related_name='liked_cars', blank=True)

    def total_likes(self):
        return self.likes.count()

    @cached_property
    def image_url(self):
        # Returns the first image URL if available
        first_image = self.images.first()
        if first_image and 'placeholder' not in first_image.image.url:
            return first_image.optimize_url
        return '/static/images/placeholder.webp'

    def __str__(self):
        return f"{self.title} | \
                  created on: {self.created_on.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ["-created_on"]
        indexes = [
            models.Index(fields=["brand"]),
            models.Index(fields=["model"]),
            models.Index(fields=["title"]),
            models.Index(fields=["category"]),
        ]


class CarImage(models.Model):
    """
    Stores a single car image entry related to :model:`car.Car`.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name='images')
    image = CloudinaryField('image', default='placeholder')

    def get_cloudinary_public_id(self):
        """
        Extract Cloudinary public ID from the image URL.
        """
        try:
            url = self.image.url
            path = urlparse(url).path
            public_id = os.path.splitext(path)[0].strip('/')
            return public_id
        except Exception as e:
            print("Failed to extract public ID:", e)
            return None

    @cached_property
    def optimize_url(self):
        """
        Replace http with https and
        inserts f_auto,q_auto and aspect ratio
        right after 'upload/' in the Cloudinary URL.
        """
        return re.sub(r'/upload/', '/upload/c_fill,w_400,h_300/f_auto,q_auto/',
                      self.image.url.replace("http://", "https://"))

    @cached_property
    def https_url(self):
        """
        Replace http with https Cloudinary URL.
        """
        return self.image.url.replace("http://", "https://")

    def __str__(self):
        return f"{self.get_cloudinary_public_id()}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`car.Car`
    and :model:`auth.User`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


@receiver(post_delete, sender=CarImage)
def delete_cloudinary_image(sender, instance, **kwargs):
    """
    Delete image from cloudinary once teh related car
    was deleted or the car image was deleted.
    """
    if instance.image:
        public_id = instance.get_cloudinary_public_id()
        if public_id:
            cloudinary.uploader.destroy(public_id)
