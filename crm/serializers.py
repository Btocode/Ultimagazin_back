from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Lead, Reflink

User = get_user_model()

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ("reflink", "email", "name")

class ReflinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflink
        fields = ("networker", "url")

    def validate(self, attrs):
        networker = attrs.get("networker", "")
        url = attrs.get("url", "")
        if Reflink.objects.filter(networker=networker, url=url).exists():
            raise serializers.ValidationError({"url": ("URL is already in use")})
        return super().validate(attrs)
        

