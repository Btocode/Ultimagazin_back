from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('v1/reflink/create/', views.CreateReflinks.as_view(), name="reflink"),
    path('v1/reflink/all/', views.GetAllRefLinks.as_view(), name="reflink"),
    path('v1/lead/create/', views.CreateLeadView.as_view(), name="create_lead"),
    path('v1/lead/delete/<int:pk>/', views.RemoveLeadView.as_view(), name="remove_lead"),
    path('v1/lead/all/', views.GetAllLeads.as_view(), name="lead"),
    path('v1/lead/all/<int:id>/', views.GetAllLeadsOfARefLink.as_view(), name="lead"),
    path('v1/reflink/delete/<int:pk>/', views.RemoveReflink.as_view(), name='remove_reflinks'),
    path('v1/networker/delete/<str:pk>/', views.RemoveNetworker.as_view(), name='remove_networker'),
    path('v1/networker/activate/<str:pk>/', views.ActivateNetworkerById.as_view(), name='activate_networker')   

]
