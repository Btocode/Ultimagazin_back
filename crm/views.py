from django.shortcuts import render
from . import serializers
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
import json, datetime, random
from .models import Lead, Reflink
from user.serializers import UserSerializer

# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()

class CreateLeadView(generics.CreateAPIView):
    '''
    Create a new lead
    '''
    serializer_class = serializers.LeadSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Get the first name and email from the request data
        name = request.data.get('name')
        email = request.data.get('email').lower()
        

        if(Lead.objects.filter(email=email).exists()):
            return Response(status = status.HTTP_200_OK, data = {'message': 'Email is already in use'})

        try:
            # Get all reflinks from the database and shuffle them
            reflinks = list(Reflink.objects.all())
            random.shuffle(reflinks)

            # Create Lead
            lead = Lead.objects.create(name=name, email=email, reflink=reflinks[0])

            # Return the lead data
            return Response(serializers.LeadInfoSerializer(lead).data)

        except Exception as e:
            # Catch the serializer error and return a 400 error response
            return Response({'error': str(e)}, status=400)

class RemoveLeadView(generics.DestroyAPIView):
    '''
    Remove a lead
    '''
    queryset = Lead.objects.all()
    serializer_class = serializers.LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateReflinks(generics.CreateAPIView):
    '''
    Create a new reflink
    '''
    queryset = User.objects.all()
    serializer_class = serializers.ReflinkSerializer

class RemoveReflink(generics.DestroyAPIView):
    '''
    Remove a reflink
    '''
    queryset = Reflink.objects.all()
    serializer_class = serializers.ReflinkSerializer
    permission_classes = [permissions.IsAuthenticated]



class GetAllRefLinks(generics.ListAPIView):
    ''' 
    Get all reflinks
    '''
    queryset = Reflink.objects.all()
    serializer_class = serializers.ReflinkInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin:
            return self.queryset.all().order_by('-created_at')

        return self.queryset.filter(networker=self.request.user).order_by('-created_at')

class GetAllLeads(generics.ListAPIView):
    ''' 
    Get all leads
    '''
    queryset = Lead.objects.all()
    serializer_class = serializers.LeadInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin:
            return self.queryset.all().order_by('-created_at')

        return self.queryset.filter(reflink__networker=self.request.user).order_by('-created_at')

class GetAllLeadsOfARefLink(generics.ListAPIView):
    ''' 
    Get all leads of a reflink
    '''
    queryset = Lead.objects.all()
    serializer_class = serializers.LeadInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        reflink_id = self.kwargs.get('id')
        print(reflink_id)
        if reflink_id:
            return self.queryset.filter(reflink=reflink_id)
        return self.queryset.none()

class RemoveNetworker(generics.DestroyAPIView):
    '''
    Remove a networker
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivateNetworkerById(generics.UpdateAPIView):
    '''
    Activate a networker by id
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            user_id = self.kwargs.get('pk')
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()
            return Response({'message': 'User activated successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)