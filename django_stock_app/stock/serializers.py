from rest_framework import serializers

from .models import Category, Product, Brand, Firm, Purchases, Sales

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

        