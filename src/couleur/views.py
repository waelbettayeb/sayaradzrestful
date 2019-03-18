from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404

from couleur.models import Couleur
from couleur.serializers import Couleur_Sereializer
from modele.models import Modele


class All_Couleur(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        return Couleur.objects.all()

class Couleur_By_Modele(ListAPIView):
    serializer_class = Couleur_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs['Id_Modele']
        return Couleur.objects.filter(Colore__Code_Modele = Id_Modele)

class New_Couleur(generics.ListCreateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = Couleur_Sereializer