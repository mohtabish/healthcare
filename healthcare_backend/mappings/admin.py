from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'is_active', 'next_appointment')
    list_filter = ('is_active', 'assigned_date', 'doctor__specialization')
    search_fields = ('patient__name', 'doctor__name')
    readonly_fields = ('assigned_date',)
    fieldsets = (
        ('Mapping Information', {
            'fields': ('patient', 'doctor', 'is_active')
        }),
        ('Additional Information', {
            'fields': ('notes', 'next_appointment')
        }),
        ('System Information', {
            'fields': ('assigned_date',)
        }),
    )