from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/v1/register/', views.RegisterAPIView.as_view(), name='register'),
    path('api/v1/networker/all/', views.GetAllNetworkers.as_view(), name='user'),
]