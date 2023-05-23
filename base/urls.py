from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response

class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "message": "Health check passed",
            "status": 200
        })

urlpatterns = [
    path('', HealthCheckView.as_view(), name='health_check'),
    path('admin/', admin.site.urls),
    path('api/', include('crm.urls'), name='api'),
    path('user/', include('user.urls'), name='user'),
]

