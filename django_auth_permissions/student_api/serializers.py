from .models import Student, Path
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    # Additional data can be added while passing database data from serializer. This added information is in the frondend section.
    # It can be displayed but not in the database.
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()

    class Meta:
        model = Student
        # fields = "__all__"  # All fields written in models.py, not very preferred
        # exclude = ["numer"]  # get all but number
        fields = ["id","first_name","last_name","number", "path","path_id","created"]  # "[]" gets anything typed, The ID is automatically issued by Django. Since models.py is not available, it may be overlooked, don't forget to write it down.


class PathSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True)

    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]