from django.db import models
from cloudinary.models import CloudinaryField


class Property(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.title
    

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()