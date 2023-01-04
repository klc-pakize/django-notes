from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

def todohome(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">TODO</h1></center>')

@api_view(['GET','POST'])
def todolist(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializers = TodoSerializer(todo, many = True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = TodoSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            message = {
                "message" : f" {serializers.data} created successfully..!"
            }
            return Response(message, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUST)


@api_view(['GET','PUT','DELETE'])
def tododetail(request, pk):
    todo = get_object_or_404(Todo, id = pk)
    if request.method == 'GET':
        serializers = TodoSerializer(todo)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializers = TodoSerializer(todo, data = request.data)
        if serializers.is_valid():
            serializers.save()
            message = {
                "message" : f" {serializers.data} updated successfully..!"
            }
            return Response(message)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUST)

    if request.method == 'DELETE':
        todo.delete()
        message = {
            "message" : f"{todo} deleted successfully..!"
        }
        return Response(message)
        

class TodoListClass(ListCreateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailClass(RetrieveUpdateDestroyAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Todos(ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer