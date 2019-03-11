from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from accounts.models import Fabriquant
from . import serializers
from . import models

class FabriquantView(ListCreateAPIView):

    serializer_class = serializers.FabriquantSerializer
    def get_queryset(self):
        return models.Fabriquant.objects.all()

class UserView(ListCreateAPIView):

    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = serializers.FabriquantSerializer(data = request.data)
        if serializer.is_valid():
            Fabriquant.objects.create_fabriquant(
                serializer.get('email'),
                serializer.get('password'),
                serializer.get('nom'),
                serializer.get('prenom'),
                serializer.get('adresse'),
                serializer.get('tel')
            )
            return Response(status= status.HTTP_201_CREATED)

        return Response(status= status.HTTP_400_BAD_REQUEST)

