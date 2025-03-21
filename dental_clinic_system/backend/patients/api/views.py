from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from patients.models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'id_number', 'medical_record_number']
    ordering_fields = ['created_at', 'first_name', 'last_name', 'age']
