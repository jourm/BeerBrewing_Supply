from django.test import TestCase
from .models import Book


# Create your tests here.


class TestProductViews(TestCase):

    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_details(self):
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')

        