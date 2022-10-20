from django.test import TestCase, Client
from .models import Hero

class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Ironman')

    def test_count(self):
        self.assertEqual(Hero.objects.all().count(),3)

    def test_index(self):
        client = Client()
        response = client.get('/hero/')
        self.assertEqual(response.status_code,200)
        self.assertIn('1',response.content.decode())

        response = client.get('/hero/')
        self.assertEqual(response.status_code,200)
        self.assertIn('2',response.content.decode())

    def test_get(self):
        client=Client()
        response = client.get('/hero/1/')

        self.assertEqual(response.status_code,200)
        self.assertIn('1',response.content.decode())