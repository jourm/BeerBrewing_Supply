from django.test import TestCase

class TestCheckout(TestCase):
    def test_terms(self):
        response = self.client.get('/checkout/terms')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/terms.html')


