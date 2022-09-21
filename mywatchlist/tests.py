from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class test(TestCase):
    def testhtml(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def testxml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def testjson(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
