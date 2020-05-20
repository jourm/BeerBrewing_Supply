from django.test import TestCase

# Create your tests here.

class TestOrders(TestCase):
    def test_order_to_ship(self):
        response = self.client.get('/orders/ready_to_ship')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/ready_to_ship.html')
