from django.test import TestCase, Client
from .models import Hero


class HeroTestCase(TestCase):
    def setUp(self) -> None:
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Spiderman')

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_assertCounter(self):
        client1 = Client()
        response = client1.get('/hero/')
        self.assertIn('1', response.content.decode())

        response = client1.get('/hero/')
        self.assertIn('2', response.content.decode())