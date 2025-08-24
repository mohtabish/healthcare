from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'created_by', 'created_at')
    list_filter = ('gender', 'created_at', 'created_by')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'date_of_birth', 'gender')
        }),
        ('Address & Medical', {
            'fields': ('address', 'medical_history')
        }),
        ('System Information', {
            'fields': ('created_by', 'created_at', 'updated_at')
        }),
    )