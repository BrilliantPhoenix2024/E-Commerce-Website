from django.test import TestCase
from django.shortcuts import reverse


class PagesTest(TestCase):
    def test_about_page_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_url(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'pages/contact.html')

    def test_contact_pages_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
