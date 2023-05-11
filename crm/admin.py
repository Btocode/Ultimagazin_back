from django.contrib import admin

# Register your models here.

from .models import Reflink, Lead

admin.site.register(Reflink)
admin.site.register(Lead)
