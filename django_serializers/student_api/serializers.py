from .models import Student, Path
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    # Additional data can be added while passing database data from serializer. This added information is in the frondend section.
    # It can be displayed but not in the database.
    born_year = serializers.SerializerMethodField()  # read only
    path = serializers.StringRelatedField() # read_only
    path_id = serializers.IntegerField()

    class Meta:
        model = Student
        # fields = "__all__"  # All fields written in models.py, not very preferred
        fields = ["id","first_name","last_name","number","age", "born_year","path","path_id"]  # "[]" gets anything typed, The ID is automatically issued by Django. Since models.py is not available, it may be overlooked, don't forget to write it down.
        # exclude = ["numer"]  # get all but number


    def get_born_year(self,obj):  # It has to start with get, followed by the same as field.
        import datetime
        current_time = datetime.datetime.now()  # current time records
        return current_time.year - obj.age

class PathSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True)

    class Meta:
        models = Path
        fields = ["id", "path_name", "students"]