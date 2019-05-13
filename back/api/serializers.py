from rest_framework import serializers
from api import models
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    review = serializers.CharField(required=True)
    rating = serializers.IntegerField(required=True)
    submission_date = serializers.DateField(required=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class FlightSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    companyName = serializers.CharField(required=True)
    sourceLocation = serializers.CharField(required=True)
    destinationLocation = serializers.CharField(required=True)
    class Meta:
        model = Flight
        fields = ('id', 'source', 'destination', 'company')

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(max_digits=10, decimal_places=6)
    location = serializers.CharField(read_only=True)
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'cost', 'location')

