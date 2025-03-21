from rest_framework import viewsets, permissions
from stomatological_exam.models import StomatologicalExam
from .serializers import StomatologicalExamSerializer

class StomatologicalExamViewSet(viewsets.ModelViewSet):
    queryset = StomatologicalExam.objects.all()
    serializer_class = StomatologicalExamSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = StomatologicalExam.objects.all()
        # Filter by patient if patient_id parameter is provided
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
