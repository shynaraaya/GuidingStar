from rest_framework import generics,status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Flight
from api.serializers import FlightSerializer

class FlightGetCreate(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.filter(id=self.kwargs['pk'])

class FlightList(APIView):
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)