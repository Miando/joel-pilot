from django.test import TestCase
from .models import ScrapedInfo


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_string_representation(self):
        items = ScrapedInfo(title="My entry title")
        self.assertEqual(str(items), items.title)
