from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization', 'experience_years', 'is_available', 'created_at')
    list_filter = ('specialization', 'is_available', 'experience_years', 'created_at')
    search_fields = ('name', 'email', 'license_number')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Professional Information', {
            'fields': ('specialization', 'experience_years', 'qualification', 'license_number')
        }),
        ('Availability & Fees', {
            'fields': ('is_available', 'consultation_fee')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )