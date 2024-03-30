from race_service_app.api.serializers import RaceSerializer
from race_service_app.models import Race
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse

class RaceListAPIView(APIView):
    def get(self, request):
        races = Race.objects.all()
        serializer = RaceSerializer(races, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class RaceDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            race = Race.objects.get(pk=pk)
        except Race.DoesNotExist:
            return Response({'Error': 'Race not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RaceSerializer(race)
        return Response(serializer.data)
    
    def put(self, request, pk):
        race = Race.objects.get(pk=pk)
        serializer = RaceSerializer(race, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self, request):
        race = Race.objects.get(pk=request.data['race_id'])
        race.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
