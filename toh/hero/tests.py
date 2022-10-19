from pydoc import cli
from django.test import TestCase, Client
from .models import Hero


class HeroTestCase(TestCase):
    def setUp(self) -> None:
        Hero.objects.create(name="Superman")
        Hero.objects.create(name="Batman")
        Hero.objects.create(name="Ironman")

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)
