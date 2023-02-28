from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Brand, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer, BrandSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.response import Response
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  ADD Product Stock ############
        
        purchase = request.data # we assign the incoming data to the variable
        product = Product.objects.get(id = purchase['product_id'])
        product.stock += purchase['quantity']
        product.save()

        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)  # we can reach the user who sent the data like this

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)        
        #! #############  UPDATE Product Stock ############
        
        purchase = request.data # we assign the incoming data to the variable
        product = Product.objects.get(id = instance.product_id)  # existing data
        conclusion = purchase['quantity'] - instance.quantity
        product.stock += conclusion
        product.save()

        #! #############################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #! #############  DELETE Product Stock ############
        
        product = Product.objects.get(id = instance.product_id)  # existing data
        product.stock += instance.quantity
        product.save()

        #! #############################################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class SalesView(ModelViewSet):

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['brand', 'product']
    search_fields = ['brand']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  REDUCE Product Stock ############
        
        sales = request.data # we assign the incoming data to the variable
        product = Product.objects.get(id = sales['product_id'])
        if sales['quantity'] <= product.stock:
            product.stock -= sales['quamtity']
            product.save()
        else:
            data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)  # we can reach the user who sent the data like this
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)        
        #! #############  UPDATE Product Stock ############
        
        sale = request.data # we assign the incoming data to the variable
        product= Product.objects.get(id=instance.product_id) 
        
        if sale["quantity"] > instance.quantity:
            
            if sale["quantity"] <= instance.quantity + product.stock:
                product.stock = instance.quantity + product.stock - sale["quantity"]
                product.save()
            else:
                data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            
        elif instance.quantity >= sale["quantity"]:
            product.stock += instance.quantity - sale["quantity"]
            product.save()

        #! #############################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        #!####### DELETE Product Stock ########

        product = Product.objects.get(id=instance.product_id)
        product.stock += instance.quantity
        product.save()

        #!##################################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)