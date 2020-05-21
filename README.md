My local Home Brewing shop has been forced to close in the wake of the coronavirus.
The purpose of this project is to create a prototype for a new website with a online shop from them.
The Shop also sells equipment and ingredients for wine and cider making,
but initially the project will only cover the beer brewing side of the business. 
A beer brewing shop has many forms of products and most of these have more sub categories,
there can for exaple be over  20 subcategoreis to Equipment. The goal of this project is not to create
all of these categories but more of a base that a full store could be built upon.


## Business goals of the site:

* Sell Equipment, ingredients, etc that are used for beer brewing.
* Promote the beerbrewing hobby

## User stories:
There are three main kinds of users.
1. Site Owner
2. Experienced Homebrewer
3. Beginner Homebrewer
1. As the site owner I want to …. So that I can ….
    * Display the products I have for sale. -- Make money
    * Post information About upcoming sales, new products, Brewing news etc -- Keep my customers informed and drive up sales 
    * Add new Products -- Sell them
2. As a Experienced Homebrewer I want to …. So that I can ….
    * Buy Ingredients for my next beer -- Brew beer
    * Advance my knowledge -- brew better beer
    * Keep track of my previous purchases. -- Know what ingredients i used last time.
    * Buy New equipment. -- Test a new method, improve my setup.
    * Buy consumables. -- Keep my equipment clean and up to date
3. As a beginner Homebrewer I  want to …. So that I can ….
    * Find relevant information easily. -- Get into the hobby
    * Find a beginner kit. -- Brew my first beer

## Features
### Navbar
* Avliable on all pages and features links for veiwing the diferent categories of products, The shopping cart, account creation and management.

### Products
The Project features a polymorfic product model with several sub classes, this was done due to the fact that a beer brewing shop
features many diferent kinds of products and the diferent products can have very different attributes. By having a Concrete Base Model with some common fields, 
the basic information such as name, Price and image, for all products can be found in the product table. The issue with this database model is that there is no simple way to know 
what sub table to look in if one only has the date from the base table. This was solved by creating a utillity function get_product() that from an id finds the product in its table.
Information and inspiration for this product model was found on [RealPython.com](https://realpython.com/modeling-polymorphism-django-python/)
Product creation is managed through the default django admin panel. When a Product is created from its sub model, records in the base and child tables are created simultaneously with 
a shared ID.
![Product Database Model](https://github.com/jourm/BeerBrewing_Supply/blob/master/media/ProductModel.PNG)
#### Hops
The Hops product inherits 
