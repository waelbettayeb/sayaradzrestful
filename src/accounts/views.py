from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from accounts.models import Fabriquant
from . import serializers
from . import models

class FabriquantView(ListCreateAPIView):

    serializer_class = serializers.FabriquantSerializer
    def get_queryset(self):
        return models.Fabriquant.objects.filter(marque = self.request.user.marque)


class AdminFabriquant(CreateAPIView):
    serializer_class = serializers.AdminFabriquantSerializer


# class UtilisateurFabriquantView(ListCreateAPIView):
#     serializer_class = serializers.UtilisateurFabrquantSerailizer
#
#     def get_queryset(self):
#         return models.UtilisateurFabriquant.objects.all()


class UserView(ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()


