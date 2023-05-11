from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Lead, Reflink

User = get_user_model()

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ("email", "name")

    def validate(self, attrs):
        email = attrs.get("email", "")
        if Lead.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)

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
        
class ReflinkInfoSerializer(serializers.ModelSerializer):
    leads = serializers.SerializerMethodField()
    networker_name = serializers.CharField(source="networker.full_name", read_only=True)
    class Meta:
        model = Reflink
        fields = "id url created_at networker leads networker_name".split()

    def get_leads(self, obj):
        # Count the number of leads for each ref link
        return Lead.objects.filter(reflink=obj).count()

class LeadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "id name email created_at reflink".split()

