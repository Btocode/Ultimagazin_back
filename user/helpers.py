from . import serializers
from django.conf import settings

def get_user_details(user):
    tokens = user.tokens
    data = {
        'user_info': serializers.UserSerializer(user).data,
        'access': tokens['access'],
        'access_token_lifetime': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
        'refresh': tokens['refresh'],
        'refresh_token_lifetime': settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
        # "is_admin": hasattr(user, 'admin')
        }
    return data