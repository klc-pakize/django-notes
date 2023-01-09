from rest_framework import serializers

from .models import Blog, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ["id","name"]


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ["id","title","content","category","status","created_date","updated_date"]
