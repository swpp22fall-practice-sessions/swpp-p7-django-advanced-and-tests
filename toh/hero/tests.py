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

    def test_hero_id(self) -> None:
        client = Client()
        response = client.get("/hero/1/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("1", response.content.decode())

    def test_visit_count(self):
        client = Client()
        client.get("/hero/")
        self.assertEqual(client.session.get("visit_count"), 1)
        client.get("/hero/")
        self.assertEqual(client.session.get("visit_count"), 2)
