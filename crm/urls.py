from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('v1/reflink/create/', views.CreateReflinks.as_view(), name="reflink"),
    path('v1/reflink/all/', views.GetAllRefLinks.as_view(), name="reflink"),
]
