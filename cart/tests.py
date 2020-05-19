from django.test import TestCase
from products.models import Product, Book
from django.urls import reverse
from . import views



class TestCartViews(TestCase):
    def test_add_to_cart(self):
        """ Tests that a product can be added to the cart and that the
        user is then redirected back to where they came from.
        This test is depandant on the Book model"""
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
        book.save()
        response = self.client.post(
            '/cart/add/'+str(book.id),
            {'amount': 1,
             'redirect_url': reverse('view_cart')})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 1})

    def test_view_cart(self):
        """ Test the cart view by creating an object, adding it to the cart
        and then visiting the view_cart and testing that the cart is avaliable
        in session and that the correct template is used
        This test is depandant on add_to_cart and the Book model"""
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
        book.save()
        self.client.post(
            '/cart/add/'+str(book.id),
            {'amount': 1,
             'redirect_url': reverse('view_cart')})
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
        self.assertEqual(self.client.session['cart'], {'1': 1})


    def test_update_cart(self):
        """ Tests that uppdate_cart works by creating a prodct,
        adding it to the cart, and the calling uppdate cart to change
        the amount of books in the cart
        This test is depandant on add_to_cart and the Book model """
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
        book.save()
        self.client.post(
            '/cart/add/'+str(book.id),
            {'amount': 1,
             'redirect_url': reverse('view_cart')})
        self.assertEqual(self.client.session['cart'], {'1': 1})
        response = self.client.post(
            '/cart/uppdate_cart/'+str(book.id),
            {'amount': 2,
             'redirect_url': reverse('view_cart')})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 2})

    def test_remove_from_cart(self):
        book = Book.objects.create(
            name='beer',
            price=10,
            author='me',
            description='book about beer'
            )
        book.save()
        self.client.post(
            '/cart/add/'+str(book.id),
            {'amount': 1,
             'redirect_url': reverse('view_cart')})
        self.assertEqual(self.client.session['cart'], {'1': 1})
        response = self.client.post(
            '/cart/delete_from_cart/'+str(book.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session['cart'], {})

