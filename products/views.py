from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Hop, Malt, Yeast, Eqipment, Book
from .utils import get_product
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    if request.GET:
        models = [["yeast", Yeast], ["malt", Malt], ["hop", Hop],
                  ["equipment", Eqipment], ["book", Book]]
        for model in models:
            if request.GET['cat'] == model[0]:
                products = model[1].objects.all()

    context = {
        'products': products,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_product(product_id)
    context = {'product': product[1], }

    return render(request, 'products/product_details.html', context)
