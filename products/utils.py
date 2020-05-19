from .models import Product, Hop, Malt, Yeast, Eqipment, Book
from django.shortcuts import get_object_or_404 


def get_product(product_id):
    """ Helper function for managing polymorphism, id are shared between the parent
    Product table and children, This function returns the corresponding child record from the parent id.
    Input: product.id of from Product table
    Output: List: [table that id was found in,
    Record from the correct child table] """
    test = Product.objects.get(pk=product_id)
    models = [["yeast", Yeast], ["malt", Malt], ["hop", Hop],
              ["eqipment", Eqipment], ["book", Book]]

    for m in models:
        try:
            if test.__getattribute__(m[0]):
                product = m[1].objects.get(pk=product_id)
                return([m[0], product])
        except:
            pass

