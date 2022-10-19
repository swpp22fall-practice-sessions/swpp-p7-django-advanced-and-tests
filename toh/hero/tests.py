from django.test import TestCase, Client

from .models import Hero

# Create your tests here.


class HeroTestCase(TestCase):
    # setUp method will be executed before each test
    def setUp(self):
        # we need new heroes for each test
        # this is because the database is not reset between tests
        Hero.objects.create(name="Superman", age=30)
        Hero.objects.create(name="Batman", age=40)
        Hero.objects.create(name="Ironman", age=50)

    def test_hero_count(self):
        hero_count = Hero.objects.count()
        self.assertEqual(hero_count, 3)

    def test_hero_id(self):
        client = Client()
        response = client.get('/hero/1/')

        self.assertEqual(response.status_code, 200)
        # is 1 in the content of the response?
        self.assertIn('1', response.content.decode())

    def test_hero_session(self):
        client = Client()
        response = client.get('/hero/')
        self.assertEqual(response.status_code, 200)
        # is 1 in the content of the response?
        self.assertIn('1', response.content.decode())
        response = client.get('/hero/')
        self.assertIn('2', response.content.decode())

    # tearDown method will be executed after each test
