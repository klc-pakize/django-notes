from django.shortcuts import render, HttpResponse

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

# class
from rest_framework.viewsets import ModelViewSet

# pagination
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

# filter
from django_filters.rest_framework import DjangoFilterBackend

# search
from rest_framework.filters import SearchFilter, OrderingFilter

def home(request):
    return HttpResponse("Student api")


#? ViewSet 
#If we use ViewSet, we have to use endpoint operations Router

class StudentMVS(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # pagination_class = CustomPageNumberPagination
    pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination

    # filterset_fields = ["first_name"]  # We add whatever we want to do the filtering process.
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["first_name", "last_name", "path"]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["first_name", "last_name", "path"]
    search_fields = ["first_name"]




class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer