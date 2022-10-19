from django.test import TestCase


class HeroTest(TestCase):
    def test_visit_count(self) -> None:
        for i in range(1, 11):
            resp = self.client.get('/hero/')
            self.assertIn(f'{i}', resp.content.decode())
