from rest_framework import serializers
from race_service_app.models import Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'
        
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Title must be at least 2 characters long.')
        else:
            return value