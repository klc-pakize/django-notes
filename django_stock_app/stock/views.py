from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Brand, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.

class CategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #! Adding the search ('?search=') attribute to the category endpoint:
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    #! Adding the search ('name=) filter attribute to the category endpoint:
    filterset_fields = ['name']

    """
    Using Django Model Permissions for Stock App Project:
    1- Create a new user from the admin panel.
    2- Create a group named Products Manages from the Groups section
    3- Allow view, delete, change and add operations for Brand, firm, category and product in the group.
    """
    #! Note: The get operation is created by default even if the user does not belong to any group.
    permission_classes = [DjangoModelPermissions]


    #! We've created a new series generator to display product details for the category when searching using the name filter at the category entry point:
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return super().get_serializer_class()

