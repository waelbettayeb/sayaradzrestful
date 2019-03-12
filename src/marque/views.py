from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
from django.core.serializers import serialize
import json

from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from marque.models import Marque
from marque.serializers import Marque_Sereializer


class ListeMarques(ListAPIView):
    serializer_class = Marque_Sereializer

    def get_queryset(self):
        return Marque.objects.all()


class NewMarque(generics.ListCreateAPIView):
    queryset = Marque.objects.all()
    serializer_class = Marque_Sereializer
    # permission_classes = (IsAdminUser,)




