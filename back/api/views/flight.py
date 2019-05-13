from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Flight
from api.serializers import FlightSerializer

class FlightList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, )
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_queryset(self):
        return Flight.objects.for_user(self.request.user)



