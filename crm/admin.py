from django.contrib import admin

# Register your models here.

from .models import Reflink, Lead, ReflinkTracker


@admin.register(Reflink)
class ReflinkAdmin(admin.ModelAdmin):
    list_display = "id networker url created_at".split()
    list_filter = "created_at".split()
    search_fields = "networker url".split()
    list_per_page = 10
    ordering = ("-created_at",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = "id name email phone created_at".split()
    list_filter = "created_at".split()
    search_fields = "name email phone".split()
    list_per_page = 10
    ordering = ("-created_at",)


@admin.register(ReflinkTracker)
class ReflinkTrackerAdmin(admin.ModelAdmin):
    list_display = ("reflink_id",)
