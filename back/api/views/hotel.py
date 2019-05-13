from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *

class HotelGetCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        return Hotel.objects.filter(id=self.kwargs['pk'])

class HotelList(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)