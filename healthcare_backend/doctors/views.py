from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    """
    List all doctors or create a new doctor
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Doctor.objects.all()
        specialization = self.request.query_params.get('specialization')
        is_available = self.request.query_params.get('is_available')
        
        if specialization:
            queryset = queryset.filter(specialization=specialization.upper())
        if is_available is not None:
            is_available_bool = is_available.lower() == 'true'
            queryset = queryset.filter(is_available=is_available_bool)
            
        return queryset

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a doctor instance
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Doctor deleted successfully'}, 
            status=status.HTTP_200_OK
        )