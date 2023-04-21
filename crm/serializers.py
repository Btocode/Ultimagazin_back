from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Lead, Reflink

User = get_user_model()

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ("")

class ReflinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflink
        fields = ("")