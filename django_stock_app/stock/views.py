from django.shortcuts import render

from .models import Category, Product, Brand, Firm, Purchases, Sales
from .serializers import CategorySerializer

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
