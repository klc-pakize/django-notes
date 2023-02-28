from rest_framework import serializers

from .models import Category, Product, Brand, Firm, Purchases, Sales

import datetime

class CategorySerializer(serializers.ModelSerializer):

    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'product_count']

    #! Method that calculates the total number of products belonging to a Category:
    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count() 

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'category_id', 'brand', 'brand_id', 'stock', 'updated', 'createds']
        read_only_fields = ['stock']

#! We have created a new serializer to display the product details for the category when searching using the name filter in the category enpoint.
class CategoryProductSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many = True)
    product_count = serializers.SerializerMethodField()
    class Meta: 
        model = Category
        fields = ['id', 'name', 'product_count', 'products']

    #! Method that calculates the total number of products belonging to a Category:
    def get_product_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count() 
    
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id','name','image']

    
class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = ['id', 'name', 'phone', 'image', 'address']

class PurchasesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

    time_hour = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = ['id', 'user', 'user_id', 'firm', 'firm_id', 'brand', 'brand_id', 'product', 'product_id', 'quantity', 'price', 'price_total', 'time_hour', 'createds', 'category']

    
    def get_category(self, obj):
        return obj.product.category.name
    
    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.createds, "%H:%M")
    
    def get_createds(self, obj):
        return datetime.datetime.strftime(obj.createds, "%d,%m,%Y")
    

class SalesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField() 
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    time_hour = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()
    
    class Meta:
        model = Sales
        fields = (
            "id",
            "user",
            "user_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            "time_hour",
            "createds",
        )
    
    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.createds, "%H:%M")
    
    def get_createds(self, obj):
        return datetime.datetime.strftime(obj.createds, "%d,%m,%Y")
    