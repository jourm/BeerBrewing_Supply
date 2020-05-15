from decimal import Decimal
from products.models import Product
from django.shortcuts import get_object_or_404


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        subtotal = quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context