from django.db import models
from products.models import Product
from django_countries.fields import CountryField

# Create your models here.



class Order(models.Model):
    order_id = models.CharField(max_length=56, null=False, editable=False)
    status = models.CharField(max_length=56, null=False, default='created')
    #user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                                 null=True, blank=True,
    #                                 related_name='orders')
    given_name = models.CharField(max_length=50, null=False, blank=False)
    family_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    klarna_line_items = models.TextField(null=False, blank=False, default='')

