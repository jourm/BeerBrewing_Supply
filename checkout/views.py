from django.shortcuts import render
from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth
import json
from products import utils
# Create your views here.

klarna_un = settings.KLARNA_UN
klarna_pw = settings.KLARNA_PW




def checkout(request):




    auth = HTTPBasicAuth(klarna_un, klarna_pw)
    headers = {'content-type': 'application/json'}
    cart = request.session.get('cart')
    total = 0
    orderlines = []
    for item in cart:
        product = utils.get_product(item)
        orderlines.append({
            'name': product[1].name,
            'product_id': product[1].id,
            'unit_price':  int(product[1].price * 100),
            'quantity': int(cart[item]),
            'tax_rate': int(00),
            'total_amount': int(product[1].price * cart[item] * 100),
            "total_tax_amount": 0
            })
        total += product[1].price * cart[item] * 100
    integer_total = int(total)
    if request.session['order_id']:
        response = requests.get(
            settings.KLARNA_BASE_URL + '/checkout/v3/orders/' +
            request.session['order_id'],
            auth=auth,
            headers=headers,
        )

        klarna_order = response.json()
        if klarna_order['order_lines'] == orderlines:
            context = {
                'klarna_order': klarna_order

            }
            return render(request, 'checkout/checkout.html', context)
        else:
            body = {
                "purchase_country": "se",
                "purchase_currency": "eur",
                "locale": "en-GB",
                "order_amount": integer_total,
                "order_tax_amount": 0,
                "order_lines": orderlines,
                "merchant_urls": {
                    "terms": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/terms",
                    "checkout": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/completed",
                    "confirmation": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/completed",
                    "push": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/orders/register_order"
                    },
                "shipping_options": [
                {
                    "id": "free_shipping",
                    "name": "Free Shipping",
                    "description": "Delivers in 5-7 days",
                    "price": 0,
                    "tax_amount": 0,
                    "tax_rate": 0,
                    "preselected": True,
                    "shipping_method": "Home"
                },
                {
                    "id": "pick_up_store",
                    "name": "Pick up at closest store",
                    "price": 399,
                    "tax_amount": 0,
                    "tax_rate": 0,
                    "preselected": False,
                    "shipping_method": "PickUpStore"
                }
                ]
            }
            data = json.dumps(body)
            response = requests.post(
                            settings.KLARNA_BASE_URL + '/checkout/v3/orders',
                            auth=auth,
                            headers=headers,
                            data=data)

            klarna_order = response.json()
            context = {
                'klarna_order': klarna_order
            }
            return render(request, 'checkout/checkout.html', context)
    else:
        cart = request.session.get('cart')
        total = 0
        orderlines = []
        for item in cart:
            product = utils.get_product(item)
            orderlines.append({
                'name': product[1].name,
                'product_id': product[1].id,
                'unit_price':  int(product[1].price * 100),
                'quantity': int(cart[item]),
                'tax_rate': int(00),
                'total_amount': int(product[1].price * cart[item] * 100),
                "total_tax_amount": 0

                })
            total += product[1].price * cart[item] * 100

        integer_total = int(total)
        body = {
            "purchase_country": "se",
            "purchase_currency": "eur",
            "locale": "en-GB",
            "order_amount": integer_total,
            "order_tax_amount": 0,
            "order_lines": orderlines,
            "merchant_urls": {
                "terms": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/terms",
                "checkout": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/completed",
                "confirmation": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/checkout/completed",
                "push": "https://8000-b75f1113-8d8d-4b56-9dba-760d8dc7771f.ws-eu01.gitpod.io/orders/register_order"
                },
            "shipping_options": [
            {
                "id": "free_shipping",
                "name": "Free Shipping",
                "description": "Delivers in 5-7 days",
                "price": 0,
                "tax_amount": 0,
                "tax_rate": 0,
                "preselected": True,
                "shipping_method": "Home"
            },
            {
                "id": "pick_up_store",
                "name": "Pick up at closest store",
                "price": 399,
                "tax_amount": 0,
                "tax_rate": 0,
                "preselected": False,
                "shipping_method": "PickUpStore"
            }
            ]
        }
        data = json.dumps(body)
        response = requests.post(
                        settings.KLARNA_BASE_URL + '/checkout/v3/orders/' +
                        request.session['order_id'],
                        auth=auth,
                        headers=headers,
                        data=data)

        klarna_order = response.json()
        context = {
            'klarna_order': klarna_order

        }
        order_id = klarna_order['order_id']
        request.session['order_id'] = order_id

        return render(request, 'checkout/checkout.html', context)


def terms(request):
    print('terms')
    return render(request, 'checkout/terms.html')


def completed(request):
    print('checkout_success')
    return render(request, 'checkout/completed.html')
