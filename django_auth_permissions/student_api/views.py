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

# permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

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

    # permission_classes = [IsAuthenticated]  #? Where we do not recognize permission_classes, we have said that now users who log in with their username and password can view that field and take action.
    permission_classes = [IsAdminUser]  #? Only Admin users can operate. Non-admin users do not have any privileges.
    # permission_classes = [IsAuthenticatedOrReadOnly]  #? The user who does not log in or register can view the data but cannot make any changes. Only registered users can make changes.


class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer