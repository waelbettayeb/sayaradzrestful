from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
from django.core.serializers import serialize
import json

from rest_framework import generics
from rest_framework.generics import ListAPIView

# Create your views here.
from modele.models import Modele
from version.models import Version
from version.serializers import Version_Sereializer


class AllVerions(ListAPIView):
    serializer_class = Version_Sereializer

    def get_queryset(self):
        return Version.objects.all()

class VersionByModele(ListAPIView):
    serializer_class = Version_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs.get('Id_Modele')
        modele = get_object_or_404(Modele, Code_Modele=Id_Modele)

        return modele.Version_set

class NewVersion(generics.ListCreateAPIView):
    queryset = Version.objects.all()
    serializer_class = Version_Sereializer
    # permission_classes = (IsAdminUser,)