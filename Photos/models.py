from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    # pub_date = models.DateTimeField(auto_now_add=True)
    # location = models.ForeignKey(Location)

class Location(models.Model):
    lacation = models.CharField(max_length =60)
    