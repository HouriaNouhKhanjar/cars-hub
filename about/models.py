from cloudinary.models import CloudinaryField
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.title