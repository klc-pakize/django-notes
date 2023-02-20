from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Brand, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
# Create your views here.

class CategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #! Adding the search ('?search=') attribute to the category endpoint:
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    #! Adding the search ('name=) filter attribute to the category endpoint:
    filterset_fields = ['name']

    #! We've created a new series generator to display product details for the category when searching using the name filter at the category entry point:
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return super().get_serializer_class()