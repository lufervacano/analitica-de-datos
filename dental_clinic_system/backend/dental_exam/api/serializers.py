from rest_framework import serializers
from dental_exam.models import DentalExam

class DentalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalExam
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
