from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *

class ReviewGetCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewRetrieve(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Review.objects.filter(id=self.kwargs['pk'])
        return queryset

def index(request):
    return render(request, 'index.html')