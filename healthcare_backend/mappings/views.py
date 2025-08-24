from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingCreateSerializer
from patients.models import Patient

class MappingListCreateView(generics.ListCreateAPIView):
    """
    List all patient-doctor mappings or create a new mapping
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user,
            is_active=True
        )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientDoctorMappingCreateSerializer
        return PatientDoctorMappingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if patient belongs to the authenticated user
            patient = serializer.validated_data['patient']
            if patient.created_by != request.user:
                return Response(
                    {'error': 'You can only assign doctors to your own patients'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            mapping = serializer.save()
            response_serializer = PatientDoctorMappingSerializer(mapping)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientMappingView(generics.ListAPIView):
    """
    Get all doctors assigned to a specific patient
    """
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        patient = get_object_or_404(Patient, id=patient_id, created_by=self.request.user)
        return PatientDoctorMapping.objects.filter(patient=patient, is_active=True)

class MappingDetailView(generics.DestroyAPIView):
    """
    Remove a doctor from a patient (soft delete)
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {'message': 'Doctor successfully removed from patient'},
            status=status.HTTP_200_OK
        )