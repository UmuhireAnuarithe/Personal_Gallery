from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length =60)

    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length =60)
    
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location,null=True)
    category = models.ForeignKey(Category,null= True)
    # pub_date = models.DateTimeField(auto_now_add=True)
    # location = models.ForeignKey(Location)
    
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