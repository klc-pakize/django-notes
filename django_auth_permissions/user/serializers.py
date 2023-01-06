from rest_framework import serializers
from django.contrib.auth.models import User  # Default User model. The User models in which the users we create are saved are included here.
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset = User.objects.all())])  # Validates whether email addresses are unique or not.
    password = serializers.CharField(write_only = True)  # write only : It will only be displayed on post and put operations. It will not appear in get transactions
    password2 = serializers.CharField(write_only = True, required = True)
 
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        )


#? With the validate function, we check whether password and password2 are the same, if not, we used raise to give an error.
    def validate(self, field):

        if field['password'] != field['password2']:

            raise serializers.ValidationError(
                {"password" : "Password fileds didn't match."}
            )
        return field


    def create(self, validated_data):

        validated_data.pop('password2')  # We will not use password2 in database, so we deleted it from Dictionary
        password = validated_data.pop('password')  # To set the password, we delete it and assign it to a variable
        user = User.objects.create(**validated_data)  # We created User with the remaining fields
        user.set_password(password)  # # The one that saves the password as encrypted to the db.
        user.save()
        return user
