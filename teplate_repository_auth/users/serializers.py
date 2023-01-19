from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True, required = True, validators=[validate_password],
    style = {'input_type':'password'})
    password2 = serializers.CharField(write_only = True, required = True, style = {'input_type':'password'})
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password", "password2")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"massega":"Password fields didint match!"}
            )
        return data


    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user