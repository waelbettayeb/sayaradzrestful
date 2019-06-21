from rest_framework import generics
from rest_framework.generics import ListAPIView

from annonce.models import Annonce
from annonce.serializers import AnnonceView_Sereializer, Annonce_Sereializer


class Annonce_Liste(generics.ListCreateAPIView):
    serializer_class = Annonce_Sereializer
    queryset = Annonce.objects.all()


class Annonce_By_Automobiliste(ListAPIView):
    """Retourne toutes les annonces d'un automobiliste"""

    serializer_class = AnnonceView_Sereializer

    def get_queryset(self):
        id_automobiliste = self.kwargs['Id_Automobiliste']
        return Annonce.objects.filter(Id_Automobiliste = id_automobiliste)



class List_All_Annonce(ListAPIView):
    serializer_class = AnnonceView_Sereializer
    def get_queryset(self):
      return Annonce.objects.all()

