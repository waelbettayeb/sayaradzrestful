from rest_framework import generics
from rest_framework.generics import ListAPIView
from CompositionVehicule.models import Vehicule_Compose
from CompositionVehicule.serializers import Compose_Sereializer,VehiculeView_Sereializer

class Compose_Vehicule(generics.ListCreateAPIView):
    serializer_class = Compose_Sereializer
    queryset = Vehicule_Compose.objects.all()


class List_All_Vehicule_Composed(ListAPIView):
    serializer_class = VehiculeView_Sereializer
    def get_queryset(self):
      return Vehicule_Compose.objects.all()
