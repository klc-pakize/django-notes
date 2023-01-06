from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView  # CreateAPIView: Used for create-only endpoints.
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


#? With the create function, when the user registers, 
#? the token will be created automatically and the token information will be displayed in the database.

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token = Token.objects.create(user_id = response.data['id'])
        response.data['token'] = token.key
        return response