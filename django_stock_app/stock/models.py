from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#! Abstract Class: If the same fields are to be found in more than one model, in order to save ourselves from repetition, an abstract class with repetitive fields is created.
class UpdateCreate(models.Model):
    createds = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


    
class Category(models.Model):

    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name
    
class Brand(models.Model):

    name = models.CharField(max_length = 25)
    image = models.TextField()

    def __str__(self):
        return self.name

class Product(UpdateCreate):

    name = models.CharField(max_length = 100, unique = True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, related_name = 'products')
    brand = models.ForeignKey(Brand, on_delete = models.SET_NULL, null = True, related_name = 'b_product')
    stock = models.SmallIntegerField(blank = True, null = True, default = 0)

    def __str__(self):
        return self.name
    

class Firm(UpdateCreate):

    name = models.CharField(max_length = 25, unique = True)
    phone = models.CharField(max_length = 25)
    address = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class Purchases(UpdateCreate):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete = models.CASCADE, related_name = 'purchases')
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'b_purchases')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'purchase')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits = 6 ,decimal_places = 2)
    price_total = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True)

    def __str__(self):
        return f" {self.product} {self.quantity}"
    

class Sales(UpdateCreate):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'b_sales')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'sale')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits = 6 ,decimal_places = 2)
    price_total = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True)

    def __str__(self):
        return f" {self.product} {self.quantity}"