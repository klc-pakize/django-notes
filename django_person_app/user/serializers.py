from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data):
        password = validated_data.pop(password)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user