from rest_framework import serializers
from .models import Flight, Hotel, FlightList, HotelList

class FlightListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
<<<<<<< HEAD


class FlightListSerializer2(serializers.ModelSerializer):
=======
>>>>>>> 5d5623dd5a8ec9205468a9d50fae7414e48cbd55
    class Meta:
        model = FlightList
        fields = ['id', 'name']

class HotelListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
<<<<<<< HEAD
    def create(self, validated_data):
        hotel = Hotel(**validated_data)
        hotel.save()
        return hotel

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dailyCost = validated_data.get('Daily Cost', instance.dailyCost)
        instance.address = validated_data.get('Address', instance.address)
        instance.city = validated_data.get('City', instance.city)
        instance.companyName = validated_data.get('Company Name', instance.companyName)
        instance.save()
        return instance

class HotelListSerializer2(serializers.ModelSerializer):
    class Meta:
        model = HotelList
        fields = ['id', 'name']

class HotelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    dailyCost = serializers.DecimalField(required=True, max_digits=6, decimal_places=6)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    companyName = serializers.CharField(required=True)

class FlightSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    companyName = serializers.CharField(required=True)
    sourceLocation = serializers.CharField(required=True)
    destinationLocation = serializers.CharField(required=True)
    departureDate = serializers.DateField(required=True)
    departureTime = serializers.TimeField(required=True)
    numSeatsRemainingEconomy = serializers.IntegerField(required=True)
    numSeatsRemainingBusiness = serializers.IntegerField(required=True)
    numSeatsRemainingFirst = serializers.IntegerField(required=True)

class FlightSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'companyName', 'sourceLocation', 'destinationLocation']

class HotelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'cost', 'city']
=======
    class Meta:
        model = HotelList
        fields = ['id', 'name']
    

>>>>>>> 5d5623dd5a8ec9205468a9d50fae7414e48cbd55
