from rest_framework import serializers
from anamnesis.models import Anamnesis

class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnesis
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
