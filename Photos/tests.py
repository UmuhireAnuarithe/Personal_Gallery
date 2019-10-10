from django.test import TestCase
from .models import Image,Category ,Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.animal= Image(image = 'passion.jpeg', name ='Animal', description='animal image')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.animal,Image))

    def test_save_image(self):
        self.travel = Image(image='travel.jpeg',name='Travel',description='travel image')
        self.travel.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_update_image(self):
        self.car = Image(image='travel.jepg',name='Toyota',description='made in Japan')
        self.car.save_image()
        cars =Image.objects.filter(name='Toyota').first()
        update= Image.objects.filter(id=cars.id).update(name='Ritico')
        updated = Image.objects.filter(name = 'Ritico').first()
        self.assertNotEqual(cars.name , updated.name)

    def test_delete_image(self):
        self.cat = Image(image='travel.jepg',name='Vox',description='made in Japan')
        self.cat.save_image()
        cat = Image.objects.filter(name='Vox').first()
        catts = Image.objects.filter(id =cat.id).delete()
        cats =Image.objects.all()
        # self.assertTrue(len(cats) == 0)