from django.contrib import admin
from .models import (
    Profile,
    Address,
    Product,
)

# Register your models here.
# To view the model in the admin panel:
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)