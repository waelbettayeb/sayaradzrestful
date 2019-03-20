from rest_framework import generics
from rest_framework.generics import ListAPIView
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




