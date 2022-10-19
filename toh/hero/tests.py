
# Create your tests here.
from pydoc import cli
from django.test import TestCase, Client
from .models import Hero

class HeroTestCase(TestCase):
    def setUp(self) -> None:
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Ironman')

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_hero_id(self) -> None:
        client = Client()
        response = client.get('/hero/1/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.content.decode())
        
    def test_hero_view_count(self) -> None:
        client = Client()
        response = client.get('/hero/')
        self.assertIn('1', response.content.decode())
        response2 = client.get('/hero/')
        self.assertIn('2', response2.content.decode())
        # response.session['visit_count']