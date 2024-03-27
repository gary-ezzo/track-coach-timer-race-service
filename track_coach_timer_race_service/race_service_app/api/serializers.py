from rest_framework import serializers
from race_service_app.models import Race

# class RaceSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     date = serializers.DateField()
#     location = serializers.CharField()
    
#     def create(self, validated_data):
#         return Race.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.date = validated_data.get('date', instance.date)
#         instance.location = validated_data.get('location', instance.location)
#         instance.save()
#         return instance
 

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'
        
    def validate_location(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Location must be at least 2 characters long.')
        else:
            return value