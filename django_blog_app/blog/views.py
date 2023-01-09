from django.shortcuts import render

from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly

# Create your views here.

class BlogMVS(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields=["title","content","category"]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['title',"content"]
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryMVS(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields=["name"]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnly]
