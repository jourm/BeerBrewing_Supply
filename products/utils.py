from .models import Product, Hop, Malt, Yeast, Eqipment, Book
from django.shortcuts import get_object_or_404 


def get_product(product_id):
    """# Write the logic that retrieve the product type"""
    test = Product.objects.get(pk=product_id)
    models = [["yeast", Yeast], ["malt", Malt], ["hop", Hop],
              ["equipment", Hop], ["book", Book]]

    for m in models:
        try:
            if test.__getattribute__(m[0]):
                product = m[1].objects.get(pk=product_id)
                return([m[0], product])
        except:
            pass

