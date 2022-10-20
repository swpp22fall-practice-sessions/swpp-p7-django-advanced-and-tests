from http import client
from urllib import response
from django.test import TestCase, Client
from .models import Hero
# Create your tests here.


class HeroTestCase(TestCase):
    def setUp(self) -> None:
        Hero.objects.create(name='ironman1')
        Hero.objects.create(name='ironman2')
        Hero.objects.create(name='ironman3')

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_hero_id(self):
        client = Client()
        response = client.get('/hero/1/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.content.decode())

    def test_response_id(self):
        client = Client()
        resp1 = client.get('/hero/1/')
        resp2 = client.get('/hero/2/')

        self.assertIn('1', resp1.content.decode())
        self.assertIn('2', resp2.content.decode())
