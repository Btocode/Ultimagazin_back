from rest_framework import serializers

from .models import CustomUser as User
from .validators import email_validator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "full_name", "is_staff", "is_active")


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=5)
    password = serializers.CharField(max_length=68, min_length=3, write_only=True)
    user_id = serializers.IntegerField(read_only=True)
    tokens = serializers.CharField(max_length=255, min_length=5, read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "user_id", "tokens"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)
        if user:
            return user
        else:
            raise AuthenticationFailed("Invalid credentials, try again")
        return super().validate(attrs)


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[email_validator])

    class Meta:
        model = User
        fields = ["email", "full_name", "password"]
