from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Car, Reservation
from .serializers import CarSerializer

# Create your views here.

class CarView(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
