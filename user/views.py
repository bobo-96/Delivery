from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.permissions import IsUserOwnerOrReadOnly
from user.serializers import ProfileSerializer, UserSerializer


class ProfileView(ModelViewSet):
    queryset = User.objects.prefetch_related('order_user')
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




