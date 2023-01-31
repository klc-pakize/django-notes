from rest_framework import serializers

from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):

    personnel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personnel_count",
        )

    def get_personnel_count(self, obj):
        return obj.personnels.count()  # Calculates the number of people belonging to a department