
#! IN THE PREVIOUS LECTURE NOTES, WE DID NOT STOP ON THESE VIEWS.PY PAGE, 
#! TODAY WE WILL PROCESS HTTP METHODS IN DETAIL 

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

#function 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#class
from rest_framework.views import APIView

def home(request):
    return HttpResponse("Student api")


########################FUNCTION BASED VIEWS###################################

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
    serializer = StudentSerializer(instance = student, data = request.data)  # instance:get student by id number  get edited student compare and make changes
    if serializer.is_valid():
        serializer.save()
        message = {
            "message" :f"{student}  update successfuly..!"
        }
        return Response(message)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, id):
    student = get_object_or_404(Student, id = id)
    student.delete()
    massage = {
        "message":f"{student} deleted successfuly..!"
    }
    return Response(message)


"""
The recommended writing method of Http Methods, 
which we have written separately above:
Those that need id are combined under a single function, and those that do not are combined under a single function.
"""


@api_view(['GET','POST'])
def studentList(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student,  many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message ={
                "message":f"{serializer.data} created successfully..!"
            }
            return Response(message,  status = status.HTTP_201_CREATED)
        return response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET','DELETE','PUT','PATCH'])
def studentDelail(request, pk):
    student = get_object_or_404(Student, id = pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(instance = student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message":f"{student} updated successfuly..!"
            }
            return Response(message)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'PATCH':
        serializer = StudentSerializer(instance = student, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = {
               "message":f"{student} updated successfuly..!"
            }
            return Response(message)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        student.delete()
        message = {
            "message":f"{student} deleted successfuly..!"
        }
        return Response(message)


########################CLASS BASED VIEWS###################################

#? APIView

class StudentListCreate(APIView):

    def get(self, request):  # It is mandatory to give http method names after def because API View will also be converted to methods.
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
               "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"
            }
            return Response(message, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class StudentListDetail(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message" : f"{student} updated successfully..!"
            }
            return Response(message)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.delete()
        message = {
            "message":f"{student} deleted successfully..!"
        }
        return Response(message)