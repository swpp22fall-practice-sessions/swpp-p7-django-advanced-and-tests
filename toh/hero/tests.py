from django.test import TestCase, Client
from .models import Hero

class HeroTestCase(TestCase):
    def test_index(self):
        client=Client()
        response=client.get('/hero/')
        self.assertEqual(response.status_code,200)
        self.assertIn('Hello, world! You visited 1 times.',response.content.decode())
        
        response=client.get('/hero/')
        self.assertEqual(response.status_code,200)
        self.assertIn('Hello, world! You visited 2 times.',response.content.decode())

