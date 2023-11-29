from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='Movie')
    desc=models.TextField()
    
    def __str__(self):
        return self.name
class Carosel(models.Model):
    image=models.ImageField(upload_to='Carosel')
    
    