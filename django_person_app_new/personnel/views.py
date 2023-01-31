from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Department
from .serializers import DepartmentSerializer
from .permissions import IsStaffOrReadOnly

# Create your views here.

class DepartmentView(ListCreateAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
