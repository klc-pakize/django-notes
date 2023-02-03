from django.db import models

# Create your models here.

class Product(models.Model):

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
    
