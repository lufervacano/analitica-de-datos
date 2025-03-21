from rest_framework import viewsets, permissions
from anamnesis.models import Anamnesis
from .serializers import AnamnesisSerializer

class AnamnesisViewSet(viewsets.ModelViewSet):
    queryset = Anamnesis.objects.all()
    serializer_class = AnamnesisSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Anamnesis.objects.all()
        # Filter by patient if patient_id parameter is provided
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
