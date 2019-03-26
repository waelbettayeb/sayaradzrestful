from rest_framework import generics
from rest_framework.generics import ListAPIView

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

class NewModele(generics.ListCreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = Modele_Sereializer
    # permission_classes = (IsAdminUser,)