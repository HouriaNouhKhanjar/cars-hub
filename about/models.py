from cloudinary.models import CloudinaryField
from django.db import models


READ = ((0, "Not Read"), (1, "Read"))


class About(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    read = models.IntegerField(choices=READ, default=0)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"message from {self.name}"
    
    class Meta:
        ordering = ["-created_on"]