from django.contrib import admin
from .models import Product, Malt, Hop, Yeast, Eqipment, Book

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
    )


class HopAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
        'alfa_acid',
        'beta_acid',
        'aroma',
        'use',
        'substitute',
    )

class MaltAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
        'malt_type',
        'description',
        'producer',

    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Hop, HopAdmin)
admin.site.register(Malt, MaltAdmin)
admin.site.register(Yeast)
admin.site.register(Eqipment)
admin.site.register(Book)

