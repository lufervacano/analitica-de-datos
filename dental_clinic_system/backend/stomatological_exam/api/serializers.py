from rest_framework import serializers
from stomatological_exam.models import StomatologicalExam

class StomatologicalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StomatologicalExam
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
