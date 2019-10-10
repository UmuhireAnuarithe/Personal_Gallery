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