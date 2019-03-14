from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Fabriquant
from . import serializers
from . import models
from . import permissions

class FabriquantView(CreateAPIView):
    permission_classes = [permissions.IsUsersOwner, IsAuthenticated]
    serializer_class = serializers.FabriquantSerializer


class ListUtilisateurFabriquantView(ListAPIView):
    serializer_class = serializers.FabriquantSerializer
    permission_classes = [permissions.IsUsersOwner, IsAuthenticated]
    lookup_field = 'marque'
    def get_queryset(self):
        id_marque = self.kwargs['Id_Marque']
        self.check_object_permissions(self.request, id_marque)
        return Fabriquant.objects.filter(marque = id_marque)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminFabriquantCreation(CreateAPIView):
    serializer_class = serializers.AdminFabriquantSerializer


class UserView(ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()


