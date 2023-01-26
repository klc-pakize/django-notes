from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#! We will show the token information along with the user information

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user = user)
        data = serializer.data
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)