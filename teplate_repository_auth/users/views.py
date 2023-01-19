from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
# Create your views here.

class RegisterAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
