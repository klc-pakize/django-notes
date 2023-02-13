from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):

    categories = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    is_in_stock = models.BooleanField(default = True)
    slug = models.SlugField(null = True, blank = True)  # When we shoot a specific object, the object is captured with a unique value such as the name of that object. We have always captured it with the id until today. Slug is also a bit of text that appears after your domain name in the URL of a page. 

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    

class Review(models.Model):

    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'reviews')
    review = models.TextField()
    is_released = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f" {self.product.name} - {self.review} "
        

