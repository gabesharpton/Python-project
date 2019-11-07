from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo_url = models.TextField()
    
    def __str__(self):
        return self.name

