from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ('assigned_date',)

class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ('patient', 'doctor', 'notes', 'next_appointment')

    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        # Check if mapping already exists and is active
        if PatientDoctorMapping.objects.filter(
            patient=patient, 
            doctor=doctor, 
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient"
            )
        
        return attrs