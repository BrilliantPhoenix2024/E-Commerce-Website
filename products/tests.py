from django.test import TestCase
from django.shortcuts import reverse

from .models import Product


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product1 = Product.objects.create(
            title='Product1',
            description='this is a description of Product1',
            active=True,
            price=106,
        )
        cls.product2 = Product.objects.create(
            title='Product2',
            description='this is a description of Product2',
            active=False,
            price=16,
        )

    # def setUp(self):

    def test_product_list_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url_by_name(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_title_on_product_list_page(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, self.product1.title)

    def test_product_detail_url(self):
        response = self.client.get(f'/products/{self.product1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url_by_name(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)

    def test_product_description_on_product_detail_page(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.id]))  # f'/products/{self.product1.id}/'
        self.assertContains(response, self.product1.title)
        self.assertContains(response, self.product1.description)

    def test_status_404_if_product_does_not_exist(self):
        response = self.client.get(reverse('product_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_active_product_is_not_true(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, self.product1.title)
        self.assertNotContains(response, self.product2.title)



