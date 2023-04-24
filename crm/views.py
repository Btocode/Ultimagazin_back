from django.shortcuts import render
from . import serializers
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
import json, datetime
from .models import Lead, Reflink

# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()

class CreateLeads(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.LeadSerializer

class CreateReflinks(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ReflinkSerializer

class GetAllRefLinks(generics.ListAPIView):
    queryset = Reflink.objects.all()
    serializer_class = serializers.ReflinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(networker=self.request.user)




