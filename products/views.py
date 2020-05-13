from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Hop, Malt, Yeast, Eqipment, Book
from .utils import get_product
# Create your views here.


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_product(product_id)
    context = {'product': product[1], }

    if product[0] == "hop":
        return render(request, 'products/hop_details.html', context)
    #elif product[0] == "malt":
    #    return render(request, 'products/malt_detail.html', context)
    #elif product[0] == "yeast":
    #    return render(request, 'products/yeast_detail.html', context)
    #elif product[0] == "equipment":
    #    return render(request, 'products/equipment_detail.html', context)
    #elif product[0] == "book":
    #    return render(request, 'products/book_detail.html', context)

