from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Brand, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer, BrandSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer

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

class BrandView(ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
class FirmView(ModelViewSet):

    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductView(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'name']
    search_fields = ['name']


class PurchasesView(ModelViewSet):
   
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['firm', 'product']
    search_fields = ['firm']
    