from rest_framework import serializers

from .models import Category, Product, Brand, Firm, Purchases, Sales

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
