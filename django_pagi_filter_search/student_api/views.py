from django.shortcuts import render, HttpResponse

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

# class
from rest_framework.viewsets import ModelViewSet

# pagination
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

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

class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer