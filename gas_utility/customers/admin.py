from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('service_type', 'status', 'submitted_at', 'resolved_at')
    search_fields = ('customer__username', 'description')
