from rest_framework import serializers
from .models import Department, Person
from django.utils import timezone

class PersonSerializer(serializers.ModelSerializer):

    departmen = serializers.StringRelatedField(read_only = True)
    departmen_id = serializers.IntegerField()
    days_since_joined = serializers.SerializerMethodField(read_only = True)
    title_name = serializers.SerializerMethodField(read_only=True)
    gender_name = serializers.SerializerMethodField(read_only=True)
    user = serializers.StringRelatedField()
    
    def get_days_since_joined(self, obj):
        return (timezone.now() - obj.start_date).days

    def get_title_name(self, obj):
        return obj.get_title_display()

    def get_gender_name(self, obj):
        return obj.get_gender_display()

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user.id
        reservation = Person.objects.create(**validated_data)
        reservation.save()
        return reservation

    class Meta:
        model = Person
        fields = (
            "id",
            "days_since_joined",
            "user",
            "first_name",
            "last_name",
            "is_staffed",
            "title",
            "title_name",
            "gender",
            "gender_name",
            "salary",
            "start_date",
            "departmen",
            "departmen_id"
        )



class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField(read_only = True)

    def get_personal_count(self, comment: Person()):
        return Person.objects.filter(departmen=comment.id).count()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personal_count",
        )

    

class DepartmentDetailSerializer(serializers.ModelSerializer):

    department = PersonSerializer(many = True,read_only=True)
    personal_count = serializers.SerializerMethodField(read_only = True)

    def get_personal_count(self, comment: Person()):
        return Person.objects.filter(departmen=comment.id).count()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "department",
            "personal_count",
            
        )