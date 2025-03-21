from rest_framework import viewsets, permissions
from dental_exam.models import DentalExam
from .serializers import DentalExamSerializer

class DentalExamViewSet(viewsets.ModelViewSet):
    queryset = DentalExam.objects.all()
    serializer_class = DentalExamSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = DentalExam.objects.all()
        # Filter by patient if patient_id parameter is provided
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
