from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254,)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                help_text='Euro,cents')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name


class Hop(Product):
    alfa_acid = models.DecimalField(max_digits=5, decimal_places=2,
                                     help_text='percent')
    beta_acid = models.DecimalField(max_digits=5, decimal_places=2,
                                    help_text='percent')
    aroma = models.CharField(max_length=512)
    use = models.CharField(max_length=512)
    substitute = models.CharField(max_length=512)


class Malt(Product):
    Base = 'Base malt'
    Caramel_crystal = 'Caramel and Crystal malt'
    Roasted_malts = 'Roasted malts'
    Grains = 'Flaked and unmalted grains'
    MALT_TYPE = [
        (Base, 'Base malt'),
        (Caramel_crystal, 'Caramel and Crystal malt'),
        (Roasted_malts, 'Roasted malts'),
        (Grains, 'Flaked and unmalted grains'),
    ]
    malt_type = models.CharField(
        max_length=100,
        choices=MALT_TYPE,
        default=Base,
    )
    description = models.CharField(max_length=512)
    producer = models.CharField(max_length=156)


class Yeast(Product):
    dosage = models.CharField(max_length=156)
    fermenting_temp = models.CharField(max_length=156)
    pitching = models.CharField(max_length=156)
    flocctuaition = models.CharField(max_length=156)
    weight = models.CharField(max_length=156)


class Eqipment(Product):
    Brewing = 'Brewing'
    Cleaning = 'Cleaning'
    Fermentation = 'Fermentation'
    Botteling = 'Botteling'
    EQ_TYPE = [
        (Brewing, 'Brewing'),
        (Cleaning, 'Cleaning'),
        (Fermentation, 'Fermentation'),
        (Botteling, 'Botteling'),
    ]
    eq_type = models.CharField(
        max_length=100,
        choices=EQ_TYPE,
        default=Brewing,
    )
    description = models.CharField(max_length=3000)


class Book(Product):
    description = models.CharField(max_length=3000)
    author = models.CharField(max_length=156)
