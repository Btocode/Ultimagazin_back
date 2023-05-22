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
    '''
    Login user
    '''
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
    '''
    Register a new user
    '''

    def post(self, request):
        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        user = User(**serializer.validated_data)
        user.set_password(password)
        print("here")
        user.save()
        print(user)
        return Response(helpers.get_user_details(user), status=status.HTTP_201_CREATED)


class GetAllNetworkers(generics.ListAPIView):
    '''
    Get all networkers
    '''

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.kwargs['status']
        if status == 'active':
            queryset = User.objects.filter(is_active=True)
        elif status == 'inactive':
            queryset = User.objects.filter(is_active=False)
        else:
            queryset = User.objects.all()
        return queryset.order_by('-date_joined')
