from django.db import models



class Property(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='properties/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()