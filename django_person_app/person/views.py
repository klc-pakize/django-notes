from django.shortcuts import get_object_or_404
from .serializers import PersonSerializer, DepartmentSerializer, DepartmentDetailSerializer
from .models import Person, Department
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import  permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsLoginOrReadOnly
from django.contrib.auth.models import User
# Create your views here.

class PersonMVS(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsLoginOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user= self.request.user)

class DepartmentMVS(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsLoginOrReadOnly]



@api_view(['GET','POST'])
@permission_classes([IsLoginOrReadOnly])
def department_list(requets):
    if requets.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentDetailSerializer()
        return Response(serializer.data)
    
    # elif requets.method == 'POST':
    #     serializer = DepartmentDetailSerializer(data = requets.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         message = {
    #             "message" : "Department created successfuly.!"
    #         }
    #         return Response(message,  status = status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
@permission_classes([IsLoginOrReadOnly])
def department_detail(request, name): 
    department = get_object_or_404(Department, name = name)
    if request.method == 'GET': 
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)
    
    # elif request.method == 'PUT':
    #     serializer = DepartmentDetailSerializer(instance=department, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         message = {
    #             "message" : "Department created successfuly.!"
    #         }
    #         return Response(message)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        message = {
            "message" : "Department created successfuly.!"
        }
        return Response(message)