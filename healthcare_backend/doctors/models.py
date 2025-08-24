from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('CARDIOLOGY', 'Cardiology'),
        ('NEUROLOGY', 'Neurology'),
        ('ORTHOPEDICS', 'Orthopedics'),
        ('PEDIATRICS', 'Pediatrics'),
        ('DERMATOLOGY', 'Dermatology'),
        ('PSYCHIATRY', 'Psychiatry'),
        ('GENERAL', 'General Medicine'),
        ('ONCOLOGY', 'Oncology'),
        ('RADIOLOGY', 'Radiology'),
        ('SURGERY', 'Surgery'),
        ('OTHER', 'Other')
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)
    experience_years = models.PositiveIntegerField()
    qualification = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.get_specialization_display()}"

    class Meta:
        ordering = ['name']