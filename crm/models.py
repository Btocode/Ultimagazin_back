from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Reflink(models.Model):
    networker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="networker"
    )
    url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.networker.email


class Lead(models.Model):
    name = models.CharField(max_length=100)
    reflink = models.ForeignKey(
        "Reflink", on_delete=models.CASCADE, related_name="reflink"
    )
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=22, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ReflinkTracker(models.Model):
    reflink_id = models.IntegerField()
    
