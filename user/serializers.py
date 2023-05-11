from rest_framework import serializers

from .models import CustomUser as User
from .validators import email_validator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "full_name", "is_staff", "is_active",'is_admin', 'date_joined')


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=5)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[email_validator])

    class Meta:
        model = User
        fields = ["email", "full_name", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)
