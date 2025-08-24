from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    specialization_display = serializers.CharField(source='get_specialization_display', read_only=True)
    
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_experience_years(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience years cannot be negative")
        if value > 50:
            raise serializers.ValidationError("Experience years seems too high")
        return value

    def validate_consultation_fee(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative")
        return value