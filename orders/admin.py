from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):


    readonly_fields = ('order_id', 'date',
                       'order_total',
                       'klarna_line_items',)

    fields = ('order_id', 'date', 'given_name', 'family_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'order_total', 'klarna_line_items')

    list_display = ('order_id', 'date', 'given_name',
                    'family_name', 'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

