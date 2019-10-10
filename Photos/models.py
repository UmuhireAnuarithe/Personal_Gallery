from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    # pub_date = models.DateTimeField(auto_now_add=True)
    # location = models.ForeignKey(Location)
    
    @classmethod
    def search_by_name(cls,search_term):
        Photos = cls.objects.filter(name__icontains=search_term)
        return Photos


class Location(models.Model):
    lacation = models.CharField(max_length =60)
    