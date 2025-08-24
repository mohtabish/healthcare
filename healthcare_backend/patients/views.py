from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    """
    List all patients for the authenticated user or create a new patient
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a patient instance
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Patient deleted successfully'}, 
            status=status.HTTP_200_OK
        )