from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length =60)
     
    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
    
    
    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()

    def filter_location(cls, filter_locale):
        """
        Function to get image by location
        """
        location_of_images = Image.objects.filter(location__id=filter_locale)
        return location_of_images

class Category(models.Model):
    category = models.CharField(max_length =60)
    
    def __str__(self):
        return self.category
        
    
    def save_category(self):
        self.save()

    
    def update_category(self):
        self.update()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location,null=True)
    category = models.ForeignKey(Category,null= True)
    # pub_date = models.DateTimeField(auto_now_add=True)
    # location = models.ForeignKey(Location)
    def __str__(self):
        return self.name
        
    @classmethod
    def search_by_category(cls,search_term):
        Photos = cls.objects.filter(category__category=search_term)
        return Photos

    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete(self):
        self.delete()