from django.shortcuts import render
from . import serializers, helpers
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import login, authenticate
import json, datetime 
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model



User = get_user_model()


# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions


class LoginAPIView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'],password=serializer.validated_data['password'])

        if user:
            return Response(helpers.get_user_details(user), status=status.HTTP_200_OK)
        data = {
            'message': 'Invalid credentials',
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        user = User(**serializer.validated_data)
        user.set_password(password)
        user.save()
        return Response(helpers.get_user_details(user), status=status.HTTP_201_CREATED)


class GetAllNetworkers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return self.queryset.filter(is_staff=True)