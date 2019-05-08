from rest_framework import serializers
from .models import Flight, Hotel, FlightList, HotelList

class FlightListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = FlightList
        fields = ['id', 'name']

class HotelListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = HotelList
        fields = ['id', 'name']
    

