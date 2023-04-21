import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from . import serializers


User = get_user_model()

def email_validator(value):
    """
    Check if user with given email already exists
    Args:
        value:
    """
    if User.objects.filter(email=value, is_active=True).exists():
        raise ValidationError("Email already exists")