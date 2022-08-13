from django.test import TestCase
from django.shortcuts import reverse


class PagesTest(TestCase):
    def test_about_page_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)