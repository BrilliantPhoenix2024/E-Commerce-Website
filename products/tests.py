from django.test import TestCase
from django.shortcuts import reverse

from .models import Product


class ProductTest(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            title='Product1',
            description='this is a description of Product1',
            active=True,
            price=106,
        )

    def test_product_list_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url_by_name(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)





