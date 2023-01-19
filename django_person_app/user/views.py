from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token = Token.objects.create(user_id=response.data['id'])
        response.data['token'] = token.key
        # print(response.data)
        return response


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})