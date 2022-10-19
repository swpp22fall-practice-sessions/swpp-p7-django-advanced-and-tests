from django.test import TestCase, Client
from .models import Hero, Team

class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='Superman', age=22, score=100)
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Ironman')
        hero = Hero.objects.get(name='Superman')
        Team.objects.create(name='Avengers', leader=hero)
    
    def test_hero_model(self):
        hero = Hero.objects.get(name='Superman')
        avengers = Team.objects.get(name='Avengers')
        avengers.members.add(hero)
        hero.introduce()
        self.assertEqual(str(hero), hero.name)
        self.assertEqual(str(avengers), avengers.name)
        

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_hero_id(self):
        client = Client()
        response = client.get('/hero/10/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('10', response.content.decode())
        
    def test_hero_name(self):
        client = Client()
        response = client.get('/hero/Superman/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Superman', response.content.decode())

    def test_index(self):
        client = Client()
        r = client.get('/hero/')
        self.assertIn('1', r.content.decode())
        r = client.get('/hero/')
        self.assertIn('2', r.content.decode())