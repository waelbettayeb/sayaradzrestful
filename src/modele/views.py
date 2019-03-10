from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
from django.core.serializers import serialize
import json
from rest_framework.generics import ListAPIView

# Create your views here.
from marque.models import Marque
from modele.models import Modele
from modele.serializers import Modele_Sereializer


class ModelesByMarque(ListAPIView):
    """Retourne tous les modèles du systeme relativement à une marque"""

    serializer_class = Modele_Sereializer

    def get_queryset(self):
        id_marque = self.kwargs['Id_Marque']
        return Modele.objects.filter(Id_Marque = id_marque)


class ListAllModels(ListAPIView):
    """Retourne tout les modèles du système"""
    serializer_class = Modele_Sereializer

    def get_queryset(self):
        return Modele.objects.all()
