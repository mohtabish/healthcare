from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

    def get_age(self, obj):
        """Calculate age from date of birth"""
        from datetime import date
        today = date.today()
        return today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)