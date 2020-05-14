from django.test import TestCase

# Create your tests here.

class TestCartViews(TestCase):

    def test_get_products(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
            

"""     def test_uppdate_cart(self):


    def test_remove_from_cart(self):

 """

