from django.shortcuts import render
from . import serializers, helpers
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import login, authenticate
import json, datetime 
from datetime import datetime
from django.conf import settings



# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions


class LoginAPIView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

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
        user = serializer.save()
        return Response(helpers.get_user_details(user), status=status.HTTP_201_CREATED)