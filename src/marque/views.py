from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
from django.core.serializers import serialize
import json
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from marque.models import Marque
from marque.serializers import MarqueSereializer


class ListeMarques(ListAPIView):
    serializer_class = MarqueSereializer

    def get_queryset(self):
        return Marque.objects.all()







