from django.test import TestCase
from .models import Image,Category ,Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.animal= Image(image = 'passion.jpeg', name ='Animal', description='animal image')
        self.technology = Category(category='Technology')
        

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

    def test_search_method(self):
        self.technology.save_category()
        images = Image.search_by_category('Technology')
        self.assertTrue(len(images) == 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(location ='Kigali')

       
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

    def test_save_location(self):
        self.musanze = Location(location ='Musanze')
        self.musanze.save_location()
        locations =Location.objects.all()
        self.assertTrue(len(locations)>0)
    
    def test_update_location(self):
        self.burera = Location(location='Burera')
        self.burera.save_location()
        cars =Location.objects.filter(location='Burera').first()
        update= Location.objects.filter(id=cars.id).update(location='Kinoni')
        updated = Location.objects.filter(location='Kinoni').first()
        self.assertNotEqual(cars.location , updated.location)

    def test_delete_location(self):
        self.burera = Location(location='Burera')
        self.burera.save_location()
        location = Location.objects.filter(location='Burera').first()
        locations = Location.objects.filter(id =location.id).delete()
        locations =Location.objects.all()
    


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.animal= Category(category='Animal')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.animal,Category))

    def test_save_category(self):
        self.car = Category(category='Cars')
        self.car.save_category()
        cars =Category.objects.all()
        self.assertTrue(len(cars)>0)
    
    def test_update_category(self):
        self.food = Category(category='Pizza')
        self.food.save_category()
        pizza =Category.objects.filter(category='Pizza').first()
        update= Category.objects.filter(id=pizza.id).update(category='Cassava')
        updated = Category.objects.filter(category='Cassava').first()
        self.assertNotEqual(pizza.category , updated.category)

    def test_delete_category(self):
        self.banana = Category(category='Fruit')
        self.banana.save_category()
        banana = Category.objects.filter(category='Fruit').first()
        fruits = Category.objects.filter(id =banana.id).delete()
        fruits =Category.objects.all()