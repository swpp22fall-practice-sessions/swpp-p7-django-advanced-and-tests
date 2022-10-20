from django.test import TestCase

from .models import Hero


class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name="Superman")
        Hero.objects.create(name="Batman")
        Hero.objects.create(name="Ironman")

    def test_hero_count(self):
        self.assertEqual(Hero.objects.count(), 3)

    def test_hero_id(self):
        response = self.client.get("/hero/10/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("10", response.content.decode())

    def test_index(self):
        # First request
        response = self.client.get("/hero/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("1", response.content.decode())

        # Second request    
        response = self.client.get("/hero/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("2", response.content.decode())
