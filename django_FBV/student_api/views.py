
#! IN THE PREVIOUS LECTURE NOTES, WE DID NOT STOP ON THESE VIEWS.PY PAGE, 
#! TODAY WE WILL PROCESS HTTP METHODS IN DETAIL 

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("Student api")

@api_view(['GET']) # default get @api_view(['GET']) == @api_view([]) 
def student_list(request):
    student = Student.objects.all()  # ORM query
    serializer = StudentSerializer(student, many = True)  # Using StudentSerializer, we converted the Quryset type from the database into a python query. The reason we say many=true is because it gives us more than one object, and if it is not written, it gives an error.
    print("serializer.data:", serializer.data)
    return Response(serializer.data)  # Data in json format is accessed by saying serializer.data



@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data = request.data)  # We reach the data from the Front End with request.data and assign it to the data variable.
    if serializer.is_valid():  # It automatically validates, 
        serializer.save()  # if validation is completed, it is saved.
        message = {
            "message" :f"{student}  created successfuly..!"
        }
        return Response(message, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_detail(request, id):  # id == pk Represents the id number from the browser
    # student = Student.objects.get(id = id)  # ORM query, .get redirects a single object
    student = get_object_or_404(Student, id = id)  # The browser will crash when an id number is not found here. We can use get_object_or_404 to avoid this.
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id = pk)
    serializer = StudentSerializer(instance = student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        massage = {
            "message" :f"{student}  update successfuly..!"
        }
        return Response(massage)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, id):
    student = get_object_or_404(Student, id = id)
    student.delete()
    massage = {
        "message":f"{student} deleted successfuly..!"
    }
    return Response(massage)