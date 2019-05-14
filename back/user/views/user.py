from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from user.serializer import UserSerializer

class UserCreateView(generics.CreateAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer


class UserListView(generics.ListAPIView):

    permission_classes =  (IsAdminUser, )

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
